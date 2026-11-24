---
name: cws-rejection-guard
description: Audits a Chrome extension against the Chrome Web Store rejection patterns before submission, using Google's own notification IDs, and returns a verdict: BLOCKED, WARN or CLEAR. Use when the user is about to submit or update an extension, when an extension was rejected and needs a fix plan, or when the user mentions a Chrome Web Store rejection, a review delay, or a permission warning.
license: MIT
---

# CWS Rejection Guard

Run this before the extension goes to the store, not after the rejection email arrives. A rejection costs days; this check costs minutes. The guard reads the package and the listing the way a reviewer does, names the exact rule behind each risk, and tells the developer what to change.

## What it checks

The pattern file beside this skill, `data/rejection-patterns.json`, holds 30 sourced patterns, each with a policy name, a Google notification ID, a severity, detection signals and a fix. Rule pack 1.0.0, verified 24 November 2026 against Google's troubleshooting page and program policies. If the pack is more than 60 days old, say so first and treat the scan as a starting point, not a verdict.

## Run order

1. **Fast path first.** If Node is available, run the bundled scanner from the extension directory: `node <skill>/guard.mjs <extension-dir>`. After the one-line install, `<skill>` is `~/.claude/skills/cws-rejection-guard`, so the command is usually `node ~/.claude/skills/cws-rejection-guard/guard.mjs <extension-dir>`. It prints every finding with its pattern id, notification ID, file and line, the fix, and a verdict line. Exit 2 means BLOCKED, exit 1 means WARN, exit 0 means CLEAR. Use its output as the working list. If Node is not available, or the extension lives on a platform where the script cannot run, perform the same checks by hand following the order below.
2. **Manifest and package.** Confirm `manifest_version` is 3. Open the submitted ZIP, not the dev folder, and confirm every file the manifest names exists with the exact same case, including icons. Confirm the package contains no minified or encoded blobs the reviewer cannot read.
3. **Remote code.** Search every `.js` and `.html` file for a script tag with an http or https source, `eval()`, the `Function` constructor on a string, and remote module imports. Any one of these is a critical finding.
4. **Permissions.** For every permission in the manifest, find the API call that uses it. A permission with no matching call is removed. Broad host permissions (`<all_urls>`, `https://*/*`) are flagged: they almost always force manual review, which takes days to weeks. Note the commonly misunderstood ones: `activeTab` is not required when broad host permissions already cover the tab, `tabs` only grants URL, title and favicon, `cookies` is not required for `document.cookie`, `storage` is not required for `localStorage`.
5. **User data.** If the code touches cookies, identity, history, bookmarks, or any remote request, the extension collects user data. Then a privacy policy must exist at a working URL in the designated Privacy Policy field, not pasted into the description, and it must describe every type of data collected, how it is used, and how it is shared. The dashboard privacy declarations must match the code, not the intention.
6. **Listing.** Read the title, description and screenshots as a stranger would. The title names the job. The description lists the major features in plain sentences. Every screenshot shows the extension doing its job. Count the most repeated content word in the description: more than 5 repetitions is keyword stuffing. Delete lists of sites, brands and locations. Delete unattributed testimonials and any claim of an award, rank or status the extension does not hold. The description cap is 16,000 characters.
7. **Single purpose.** Describe the extension in one sentence. If you cannot, or if two features could each stand alone as their own product, the extension must be split. Ad injection bundled with anything else is a rejection on its own.
8. **Deception and prohibited products.** Every promised feature must work, and every behavior must be mentioned in the metadata. YouTube downloads, paywall bypasses and login bypasses cannot be listed at all. Affiliate links need disclosure in the description and the UI, and a related user action before inclusion.
9. **Functionality.** Install the submitted ZIP in a clean Chrome profile and use every feature once. A server the extension needs must be up. If a feature needs an account, leave working test credentials in the reviewer notes field.

## Output

Report in this order, and no other order:

1. The verdict line: `BLOCKED`, `WARN` or `CLEAR`, with the count of critical, high and medium findings.
2. Findings in severity order, each with the pattern id, the notification ID, the file and line, what is wrong in the developer's own words, and the fix.
3. The checks only a person can do: single purpose, deception, whether the extension works in a clean profile, whether the screenshots are honest.
4. One closing line, always: what this scan cannot prove, and that CLEAR is not an approval.

## Rules

- Never say the extension will pass. Say what the scan found and what it cannot see.
- Never invent a pattern. Every finding cites a pattern id from the file, and every pattern cites a Google page.
- A finding without a file and line, or without a fix, is not a finding. Go and find the evidence.
- When the extension was already rejected, start from the rejection email: map each cited violation to its pattern id, fix exactly that, and use the reviewer notes field to explain the change on resubmission. If the rejection looks wrong, the appeal goes through the Chrome Web Store One Stop Support form, and the appeal states the policy by name, the evidence that the flagged permission maps to a visible feature, and a screenshot or short recording of that feature working.
