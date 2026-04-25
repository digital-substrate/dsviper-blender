---
name: git-safety
description: Prevents unauthorized git operations. Use before any git commit, push, merge, rebase, reset, or other state-changing git commands. Requires explicit user approval for all commits.
model: haiku
allowed-tools: Bash, AskUserQuestion
---

# Git Safety Skill

## Golden Rule

**NEVER commit without explicit user approval.**

Even if the user asked to "fix the bug" or "add the feature", completing the task does NOT
imply permission to commit. A commit requires a separate, explicit request.

## Operations Requiring User Approval

### ALWAYS ask before:

| Operation               | Risk Level | Approval Required          |
|-------------------------|------------|----------------------------|
| `git commit`            | Medium     | YES - always               |
| `git push`              | High       | YES - always               |
| `git merge`             | High       | YES - always               |
| `git rebase`            | Critical   | YES - always               |
| `git reset --hard`      | Critical   | YES + confirmation         |
| `git checkout <branch>` | Medium     | YES if uncommitted changes |
| `git stash drop`        | High       | YES - always               |
| `git branch -D`         | High       | YES - always               |

### Safe operations (no approval needed):

- `git status`
- `git log`
- `git diff`
- `git branch` (list only)
- `git stash` (save)
- `git stash list`
- `git fetch`

## Approval Workflow

### Step 1: Prepare the commit

When work is complete, show the user:

```
git status
git diff --staged
```

### Step 2: Ask for approval

Use AskUserQuestion or ask directly:

```
Work complete. Ready to commit?

Changes:
- [list modified files]

Proposed commit message:
"type(scope): description"

Options:
1. Commit with this message
2. Modify the message
3. Don't commit yet
```

### Step 3: Wait for explicit response

Only proceed if user says:

- "Yes", "OK", "Commit", "Go ahead"
- "Commit with message: ..."
- Selects option 1 or 2

Do NOT interpret these as commit approval:

- "Looks good" (might refer to the code, not commit intent)
- "Thanks" (acknowledgment, not instruction)
- "Perfect" (appreciation, not command)
- Silence or moving to next topic

## Commit Message Format

Follow project conventions:

```
type(scope): description

[optional body]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`

## Forbidden Operations

**NEVER execute without explicit user request:**

- `git push --force` (destructive)
- `git reset --hard` to remote commits
- `git rebase` on pushed branches
- `git commit --amend` on pushed commits
- Any operation that rewrites public history

## Recovery Guidance

If user needs to undo:

```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Recover dropped stash (within ~30 days)
git fsck --no-reflog | grep commit
```

## Checklist Before Commit

- [ ] User explicitly requested commit
- [ ] All changes are intentional (no debug code, no temp files)
- [ ] No secrets in staged files (.env, credentials, API keys)
- [ ] Commit message follows format
- [ ] Correct branch (not committing to main by accident)
