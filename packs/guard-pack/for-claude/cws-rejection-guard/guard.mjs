#!/usr/bin/env node
// cws-rejection-guard: pre-submission scan for Chrome Web Store rejections.
// Zero dependencies, Node 18 or newer. Reads an extension directory and an
// optional listing file, checks it against data/rejection-patterns.json, and
// prints a verdict. Exit 2 means BLOCKED (a critical finding), exit 1 means
// WARN (high findings, no critical), exit 0 means CLEAR. CLEAR is not an
// approval: the reviewer still checks what a scan cannot see.
import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { join, dirname, resolve, extname } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const DB = JSON.parse(readFileSync(join(HERE, 'data', 'rejection-patterns.json'), 'utf8'));
const BY_ID = Object.fromEntries(DB.patterns.map((p) => [p.id, p]));

const PERMISSION_API = {
  tabs: /chrome\.tabs\./,
  cookies: /chrome\.cookies\./,
  storage: /chrome\.storage\./,
  history: /chrome\.history\./,
  bookmarks: /chrome\.bookmarks\./,
  downloads: /chrome\.downloads\./,
  notifications: /chrome\.notifications\./,
  alarms: /chrome\.alarms\./,
  scripting: /chrome\.scripting\./,
  webNavigation: /chrome\.webNavigation\./,
  webRequest: /chrome\.webRequest\./,
  identity: /chrome\.identity\./,
  contextMenus: /chrome\.contextMenus\./,
  declarativeNetRequest: /chrome\.declarativeNetRequest\./,
  sidePanel: /chrome\.sidePanel\./,
  management: /chrome\.management\./,
  clipboardRead: /navigator\.clipboard|document\.execCommand\(['"]copy/,
  clipboardWrite: /navigator\.clipboard|document\.execCommand\(['"]copy/,
  favicon: /chrome\.favicon\./,
  sessions: /chrome\.sessions\./,
  tabGroups: /chrome\.tabGroups\./,
};

const DATA_SIGNALS = [
  /chrome\.cookies\./,
  /chrome\.identity\./,
  /chrome\.history\./,
  /chrome\.bookmarks\./,
  /fetch\(\s*['"]https?:\/\//,
  /XMLHttpRequest/,
];

function walk(dir, out = []) {
  for (const e of readdirSync(dir)) {
    const full = join(dir, e);
    if (e === 'node_modules' || e.startsWith('.')) continue;
    const st = statSync(full);
    if (st.isDirectory()) walk(full, out);
    else if (['.js', '.html', '.css', '.json'].includes(extname(full))) out.push(full);
  }
  return out;
}

function linesOf(path) {
  try { return readFileSync(path, 'utf8').split('\n'); } catch { return []; }
}

function main() {
  const args = process.argv.slice(2);
  const asJson = args.includes('--json');
  const positional = args.find((a) => !a.startsWith('--'));
  if (!positional) {
    console.error('Usage: node guard.mjs <extension-dir> [--json]');
    console.error('Give the folder that holds manifest.json.');
    process.exit(2);
  }
  const target = resolve(positional);
  const findings = [];
  const manual = [];
  const add = (id, file, line, detail) => {
    const p = BY_ID[id];
    findings.push({ id, severity: p.severity, notification: p.notification, family: p.family, file, line, detail: detail || p.signals[0], fix: p.fix });
  };

  const manifestPath = join(target, 'manifest.json');
  if (!existsSync(manifestPath)) {
    console.log('CWS Rejection Guard: no manifest.json found in ' + target);
    process.exit(2);
  }
  let manifest;
  try { manifest = JSON.parse(readFileSync(manifestPath, 'utf8')); } catch {
    console.log('CWS Rejection Guard: manifest.json is not valid JSON.');
    process.exit(2);
  }

  const files = walk(target).filter((f) => f !== manifestPath);
  const code = files.map((f) => ({ path: f, text: readFileSync(f, 'utf8') }));
  const allText = code.map((c) => c.text).join('\n');
  const rel = (f) => f.slice(target.length + 1);

  // CWS-004: Manifest V3 is required for new submissions.
  if (manifest.manifest_version !== 3) add('CWS-004', 'manifest.json', 1, 'manifest_version is ' + manifest.manifest_version + ', not 3.');

  // CWS-005: every file the manifest names must exist, with the exact case.
  const named = [];
  const icons = { ...(manifest.icons || {}), ...(manifest.action?.default_icon || {}), ...(manifest.browser_action?.default_icon || {}) };
  for (const [size, p] of Object.entries(icons)) if (typeof p === 'string') named.push(p);
  if (manifest.background?.service_worker) named.push(manifest.background.service_worker);
  if (manifest.action?.default_popup) named.push(manifest.action.default_popup);
  if (manifest.options_page) named.push(manifest.options_page);
  if (manifest.options_ui?.page) named.push(manifest.options_ui.page);
  for (const cs of manifest.content_scripts || []) for (const f of [...(cs.js || []), ...(cs.css || [])]) named.push(f);
  for (const r of manifest.web_accessible_resources || []) for (const f of r.resources || []) named.push(f);
  for (const p of named) {
    if (!existsSync(join(target, p))) add('CWS-005', 'manifest.json', 1, 'Named file is missing from the package: ' + p);
  }

  // CWS-001, CWS-002: remote code.
  for (const { path, text } of code) {
    linesOf(path).forEach((ln, i) => {
      if (/<script[^>]+src=["']https?:\/\//i.test(ln)) add('CWS-001', rel(path), i + 1, 'Script tag loads code from outside the package.');
      if (/\beval\s*\(/.test(ln)) add('CWS-001', rel(path), i + 1, 'eval() on a string.');
      if (/new\s+Function\s*\(/.test(ln)) add('CWS-001', rel(path), i + 1, 'Function constructor on a string.');
      if (/import\s*\(\s*['"]https?:\/\//.test(ln) || /from\s+['"]https?:\/\//.test(ln)) add('CWS-002', rel(path), i + 1, 'Module imported from a remote URL.');
    });
  }

  // CWS-003: obfuscation.
  for (const { path, text } of code) {
    const escapes = (text.match(/\\x[0-9a-fA-F]{2}|\\u[0-9a-fA-F]{4}/g) || []).length;
    if (escapes > 20) add('CWS-003', rel(path), 1, escapes + ' hex or unicode escapes in one file.');
    for (const [i, ln] of linesOf(path).entries()) {
      if (ln.length > 500 && /^[A-Za-z0-9+/=]{500,}$/.test(ln.trim())) add('CWS-003', rel(path), i + 1, 'A line over 500 characters of base64-like text.');
    }
  }

  // CWS-007: unused permissions. CWS-009: debug-only permissions.
  const declared = [...(manifest.permissions || []), ...(manifest.optional_permissions || [])];
  for (const perm of declared) {
    const re = PERMISSION_API[perm];
    if (re && !re.test(allText)) add('CWS-007', 'manifest.json', 1, 'Permission "' + perm + '" is declared but never used in the code.');
    if (!re && !['activeTab'].includes(perm)) manual.push('Permission "' + perm + '" has no API mapping in this guard; confirm by hand that the code uses it.');
  }
  if (declared.includes('activeTab') && (manifest.host_permissions || []).some((h) => h.includes('*'))) {
    add('CWS-007', 'manifest.json', 1, 'activeTab is declared alongside broad host permissions that already cover the same access; it is not required.');
  }

  // CWS-008: overbroad host permissions.
  for (const h of manifest.host_permissions || []) {
    if (h === '<all_urls>' || h === 'https://*/*' || h === 'http://*/*' || h === '*://*/*') add('CWS-008', 'manifest.json', 1, 'Host permission "' + h + '" is as broad as it gets.');
  }
  for (const cs of manifest.content_scripts || []) {
    for (const m of cs.matches || []) if (m === '<all_urls>') add('CWS-008', 'manifest.json', 1, 'A content script matches <all_urls>.');
  }

  // CWS-025: prohibited products, YouTube download proxy.
  if (/youtube\.com|youtu\.be/.test(allText) && /chrome\.downloads\./.test(allText)) {
    add('CWS-025', 'manifest.json', 1, 'The code touches YouTube and the downloads API in the same package.');
  }

  // CWS-022: affiliate links without disclosure.
  const listingPath = join(target, 'listing.json');
  let listing = null;
  if (existsSync(listingPath)) { try { listing = JSON.parse(readFileSync(listingPath, 'utf8')); } catch { listing = null; } }
  const affiliate = /amzn\.to|amazon\.[a-z.]+\/dp\/|tag=[a-z0-9-]{5,}|affiliate/i.test(allText);
  if (affiliate && listing && !/affiliate/i.test(listing.description || '')) {
    add('CWS-022', 'listing.json', 1, 'Affiliate links appear in the code but the description never discloses them.');
  }

  // Listing checks: CWS-010, CWS-018, CWS-028, CWS-013.
  if (listing) {
    const desc = listing.description || '';
    if (!desc.trim()) add('CWS-010', 'listing.json', 1, 'The description is blank.');
    if (!listing.title || !listing.title.trim()) add('CWS-010', 'listing.json', 1, 'The title is blank.');
    if (!listing.screenshots || listing.screenshots.length === 0) add('CWS-010', 'listing.json', 1, 'No screenshots listed.');
    if (desc.length > 16000) add('CWS-028', 'listing.json', 1, 'The description is ' + desc.length + ' characters; the cap is 16,000.');
    const words = desc.toLowerCase().replace(/[^a-z0-9\s]/g, ' ').split(/\s+/).filter((w) => w.length > 3);
    const stop = new Set(['with', 'your', 'that', 'this', 'from', 'have', 'will', 'more', 'when', 'than', 'also', 'into', 'over', 'your']);
    const counts = {};
    for (const w of words) if (!stop.has(w)) counts[w] = (counts[w] || 0) + 1;
    const top = Object.entries(counts).sort((a, b) => b[1] - a[1])[0];
    if (top && top[1] > 5) add('CWS-018', 'listing.json', 1, 'The word "' + top[0] + '" appears ' + top[1] + ' times in the description.');
    const domains = (desc.match(/[a-z0-9-]+\.(com|net|org|io|app|dev)/gi) || []).length;
    if (domains > 5) add('CWS-018', 'listing.json', 1, 'The description lists ' + domains + ' site names.');
  } else {
    manual.push('No listing.json found next to the extension, so the listing checks did not run. Create one with title, description, screenshots and privacy policy URL, or check the dashboard fields by hand.');
  }

  // CWS-013: data collection without a privacy policy.
  const collects = DATA_SIGNALS.some((re) => re.test(allText));
  const policyUrl = listing?.privacy_policy_url || '';
  if (collects && !policyUrl) {
    add('CWS-013', 'listing.json', 1, 'The code touches user data (cookies, identity, history, or a remote request) but no privacy policy URL is set.');
  }
  if (collects && policyUrl) manual.push('A privacy policy URL is set; open it and confirm it describes every type of data the code collects, how it is used, and how it is shared.');

  // Manual checks the scan cannot prove.
  manual.push('Single purpose: describe the extension in one sentence. If you cannot, or if two features could each stand alone as their own product, split it (CWS-017).');
  manual.push('Deceptive behavior: read the listing next to the code. Every promised feature must work, and every behavior must be mentioned (CWS-011).');
  manual.push('Functionality: install the submitted ZIP in a clean Chrome profile and use every feature once. A server the extension needs must be up (CWS-006, CWS-030).');
  manual.push('Screenshots: each one must show the extension doing its job, not a stock image (CWS-010).');

  const crit = findings.filter((f) => f.severity === 'critical').length;
  const high = findings.filter((f) => f.severity === 'high').length;
  const med = findings.filter((f) => f.severity === 'medium').length;
  const verdict = crit ? 'BLOCKED' : high ? 'WARN' : 'CLEAR';
  const verifiedOn = new Date(DB.verified_on + 'T00:00:00Z');
  const ageDays = Math.floor((Date.now() - verifiedOn.getTime()) / 86400000);
  const stale = ageDays > DB.stale_after_days;

  if (asJson) {
    console.log(JSON.stringify({ rule_pack: DB.rule_pack, version: DB.version, verified_on: DB.verified_on, stale, verdict, counts: { critical: crit, high, medium: med }, findings, manual_checks: manual }, null, 2));
  } else {
    console.log('CWS Rejection Guard, rule pack ' + DB.version + ' (verified ' + DB.verified_on + ', ' + ageDays + ' days old)' + (stale ? '  Rule pack STALE: update it before trusting this scan.' : ''));
    console.log('Extension: ' + target);
    console.log(verdict + '. ' + crit + ' critical, ' + high + ' high, ' + med + ' medium.');
    console.log('');
    const order = { critical: 0, high: 1, medium: 2 };
    for (const f of findings.sort((a, b) => order[a.severity] - order[b.severity])) {
      console.log('[' + f.severity.toUpperCase() + '] ' + f.id + ' · ' + f.notification + ' · ' + f.file + (f.line ? ':' + f.line : ''));
      console.log('  ' + f.detail);
      console.log('  Fix: ' + f.fix);
    }
    if (!findings.length) console.log('No mechanical findings. That is not an approval.');
    console.log('');
    console.log('Checks only a person can do:');
    for (const m of manual) console.log('  - ' + m);
    console.log('');
    console.log('What this scan cannot prove: whether the extension works when the reviewer runs it, whether its server is up at review time, whether a screenshot honestly shows the product, or whether a reviewer will accept a permission justification.');
  }
  process.exit(crit ? 2 : high ? 1 : 0);
}

main();
