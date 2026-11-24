## Skill: Backup Before Change

> Makes a restore point of your skills, configs and dotfiles before an AI agent edits them, and rolls back cleanly when an edit goes wrong. Use when the user is about to let an AI modify configuration, skills, shell profiles or any setup that took time to tune.

# Backup Before Change

Agents edit fast, broadly and confidently. A config that took you months to tune can be rewritten in one pass, including the parts nobody mentioned. Undo only exists if a copy was made first, somewhere the agent is not editing. Make the restore point before the session starts, not after something looks wrong.

## Know your surface

List what the agent may touch before it touches anything:

- Skills and rule folders for every AI you use
- Agent and editor configs, settings files, keybindings
- Dotfiles: shell profiles, `.gitconfig`, SSH and terminal configs
- The project files in scope for the session

If you cannot name the surface, the first task is a listing, not an edit.

## Snapshot

Pick one of these, in order of preference:

1. **Git.** Keep configs and skills in a private repo. Before the session: `git add -A && git commit -m "restore point before agent session"`. Every later state is one checkout away.
2. **Dated copy.** Copy the folders somewhere outside the working area, named with the date and the reason: `cp -R ~/.claude ~/backups/claude-2026-11-22-before-skill-edit`. Outside matters: a backup inside the edited folder gets edited too.
3. **Archive.** For a whole home setup, one compressed archive of the listed folders, stored on another drive or in cloud storage.

State the snapshot location and the exact restore command out loud, in the chat, before editing begins. A backup nobody can find is not a backup.

## Work in a way that can be undone

- One change at a time. Ask for the smallest edit, then look at the diff before approving the next one.
- A diff you cannot explain is a rollback candidate, even if things still seem to work.
- After each change, verify the thing itself: open the app, run the command, load the skill. "The file was updated" is not verification.

## Roll back cleanly

1. Stop the agent. Do not let it "fix" a bad state by editing more of it.
2. Restore the whole folder from the snapshot rather than hand-repairing individual lines. Hand repairs leave a mix of two states that nobody fully understands.
3. Verify the restored setup works.
4. Re-apply only the edits you still want, one at a time, checking each.

## Housekeeping

Keep the last few snapshots and delete older ones on a simple rule, such as one per week for a month. Note in the snapshot name what prompted it, so future you knows which one holds the good state.

## Output

Before any editing: the snapshot location, what it covers, and the restore command. After a rollback: what was restored, what was verified working, and which edits were re-applied.

---

## Skill: Secrets Out

> Scrubs credentials, tokens, personal data and private paths out of text and files before they are pasted into an AI chat, committed to a repo or sent to anyone. Use when the user is about to share code, logs, configs or screenshots outside their own machine.

# Secrets Out

Treat anything pasted into a chat, committed to a repo or attached to a message as published. It may be logged, indexed, forwarded or trained on. You cannot unpaste. So the scrub happens before sharing, every time, as a deliberate pass, not a hopeful glance.

## What counts as a secret

- API keys, access tokens, session cookies and authorization headers
- Passwords, including the ones inside connection strings and URLs
- Private keys, certificates and the full contents of `.env` files
- Personal data: email addresses, phone numbers, home addresses, ID numbers, client and patient names
- Private paths and names: your home directory path gives away your username, internal hostnames and admin URLs map someone else's network
- Screenshots and logs, which carry all of the above while looking harmless

## Method

1. **Search before you share.** Run a search over the exact text or files you are about to send. Useful patterns: `sk-`, `AKIA`, `Bearer `, `password`, `token`, `secret`, `PRIVATE KEY`, `@` for stray email addresses. Read every hit in context.
2. **Replace, do not just delete.** Swap each real value for a labelled placeholder that keeps the shape: `API_KEY_HERE`, `user@example.com`, `postgres://user:password@host/db` becomes `postgres://USER:PASSWORD@HOST/DB`. The AI still understands the structure, and nothing real leaves the machine.
3. **Keep the mapping private, if at all.** If you must restore real values later, keep the mapping in a local note that is never part of what you share. Most of the time you do not need it: retype the real value yourself at the end.
4. **Check history, not just the file.** In a repo, a secret removed in the latest commit still sits in every earlier commit and every clone. Search the history before pushing anything public.
5. **Rotate what already leaked.** If a real key has already been pasted or pushed, redaction is not a fix. Issue a new key and revoke the old one. That is the only step that actually closes the hole.

## Habits that prevent the problem

- Keep secrets in environment variables or a local `.env` file that is listed in `.gitignore` from the first commit, never in code, skills or notes.
- Give the AI the shape of the data, not the data: sample rows with fake names teach it everything real rows would.
- Make the scrub the last step before paste or commit, the way you check a pocket before laundry.

## Output

The scrubbed text, a short list of what was replaced, and a separate warning for anything that was already exposed and needs rotating.

---

## Skill: Vet Before Install

> Vets a third-party skill or prompt pack before it goes anywhere near your AI: an automated audit first, then the human checks that catch what scanners miss. Use when the user is about to install a skill, prompt pack, rule file or agent config written by someone else.

# Vet Before Install

A skill is not a document. It is a set of instructions your AI will follow with your permissions, on your files, sometimes on every future task. Installing one you have not read is running a stranger's script, just written in prose. Vet it first. Ten minutes now beats one bad afternoon later.

## The automated pass

Run a scanner before you read a word. It is fast, it is boring, and it catches the loud problems.

1. Download the pack into a holding folder, not into your skills directory.
2. Run [SkillClinic](https://github.com/Dongdarealest/skillclinic) against that folder. It checks the files for invalid structure, instructions that reach for credentials or private data, commands that download and run remote code, override language, and skills that conflict with each other.
3. Read every finding. A FAIL means fix it yourself or walk away. A WARN means you understand exactly what triggers it before you proceed. A clean scan is a starting point, not a verdict.

## The human checks

Scanners match patterns. These five checks catch intent, which is where the real risk lives.

1. **Authority claims.** Search the text for lines that tell the AI to ignore its other instructions, keep secrets from you, or treat this file as the highest authority. A skill that outranks you is not a skill, it is a takeover.
2. **Outbound actions.** List everything the skill tells the AI to send, post, upload, publish or delete, and where. Each one needs a reason you would accept if a colleague proposed it.
3. **Credential reach.** Note every file, folder and variable the skill wants read: environment files, SSH keys, browser data, cloud tokens, password managers. A formatting skill needs none of these.
4. **Persistence.** Check whether the skill edits your config, your shell profile, other skills or itself. Anything that installs a foothold survives the conversation and deserves the hardest look.
5. **Description versus body.** The frontmatter description is the advertisement. Read the body and confirm it does only what the description promises. A mismatch in either direction is a reason to stop.

## Provenance and trial

- Prefer a public repo you can inspect over a file passed around in chats. Check who published it, whether it is maintained, and whether issues or comments mention surprises.
- Confirm the copy you downloaded matches the repo. Files forwarded through chats get edited in transit.
- Trial it contained: a throwaway project, a harmless task, no real accounts. Watch what it actually does, not what it says it does.
- Install it yourself, into the real skills folder, only after all of the above.

## Output

A verdict in one line: install, install edited, or reject. Then the findings that drove it, what you removed if you edited it, and anything that still needs watching after install.
