# Advanced Git: Recovery, History & Releases

## Overview

Git provides several powerful features to recover from mistakes, manage unfinished work, rewrite commit history, and mark official releases.

Understanding **when** to use these commands is just as important as knowing **how** to use them. These topics are frequently discussed in technical interviews because they reflect real-world collaboration and version control practices.

---

# Module Topics

- Git Stash
- Git Restore
- Git Reset
- Git Revert
- Git Merge vs Git Rebase
- Git Clean
- Git Tags

---

# Git Stash

## What is Git Stash?

Git Stash temporarily saves your uncommitted work so you can switch branches or work on another task without creating an incomplete commit.

Think of it as a temporary shelf where Git stores your unfinished work.

---

## When should you use Git Stash?

Example:

- You're developing a new feature.
- Your manager asks you to fix a production bug immediately.
- Your changes are incomplete and shouldn't be committed yet.

Instead of committing unfinished work:

```bash
git stash
```

Git stores your changes and restores your working directory to the last committed state.

---

## Stash Workflow

```
Working Directory
        │
        ▼
   git stash
        │
        ▼
 Stash Storage

Working Directory becomes clean
```

---

## Common Stash Commands

### Save current work

```bash
git stash
```

---

### View all stashes

```bash
git stash list
```

Example:

```text
stash@{0}
stash@{1}
stash@{2}
```

---

### Restore and remove the latest stash

```bash
git stash pop
```

Equivalent to:

> Restore + Delete

---

### Restore but keep the stash

```bash
git stash apply
```

Useful when you may need the same stash again.

---

### Delete a stash

```bash
git stash drop stash@{0}
```

---

# Git Restore

## What is Git Restore?

Git Restore is used to discard unwanted changes or remove files from the staging area.

---

## Restore a File

Discard local modifications.

```bash
git restore app.txt
```

The file returns to its last committed state.

---

## Restore All Files

```bash
git restore .
```

Discard every uncommitted change.

---

## Unstage a File

Remove a file from the staging area while keeping your edits.

```bash
git restore --staged app.txt
```

```
Staging Area
      │
      ▼
Working Directory
```

Your code remains unchanged.

---

## Restore Working Directory Only

```bash
git restore --worktree .
```

Discard working directory changes while preserving staged files.

---

# Git Reset vs Git Revert

This is one of the most common Git interview questions.

---

# Git Revert

## What is Git Revert?

Git Revert creates a **new commit** that reverses the changes introduced by an earlier commit.

History remains intact.

```bash
git revert <commit-id>
```

Example:

```
Commit A
Commit B
Commit C

git revert Commit C

↓

Commit A
Commit B
Commit C
Commit D (undoes C)
```

---

## When should you use Revert?

Use Revert on:

- Shared repositories
- Team projects
- Public branches
- Production branches

Because it preserves project history.

---

# Git Reset

## What is Git Reset?

Git Reset moves the branch pointer (HEAD) back to an earlier commit.

Unlike Revert, Reset **rewrites history**.

Never use Reset on shared branches.

---

## Soft Reset

```bash
git reset --soft HEAD~1
```

Result:

- Last commit removed
- Changes remain staged

```
Commit Removed

↓

Files still staged
```

Useful when you simply want to rewrite the commit.

---

## Hard Reset

```bash
git reset --hard HEAD~1
```

Result:

- Commit removed
- Staging area cleared
- Working directory restored

Everything after that commit is permanently deleted.

⚠️ Use with caution.

---

# Reset vs Revert

| Git Reset | Git Revert |
|------------|------------|
| Rewrites history | Preserves history |
| Removes commits | Creates a new commit |
| Use on private branches | Use on shared branches |
| Dangerous if pushed | Safe for collaboration |

---

# Git Merge vs Git Rebase

Both commands combine work from different branches.

Their approach is different.

---

# Git Merge

```
main

A──B──C
       \
        D──E feature

git merge

A──B──C────M
       \  /
        D─E
```

Git creates a new Merge Commit.

Advantages:

- Safe
- Preserves history
- Easy to understand

Disadvantage:

Lots of merge commits.

---

# Git Rebase

```
Before

main

A──B──C

feature

A──B──D──E

git rebase main

↓

main

A──B──C

feature

A──B──C──D'──E'
```

Git moves your commits on top of the latest main branch.

Advantages:

- Clean history
- Linear commits
- Easier to read

Disadvantages:

- Rewrites history
- Changes commit IDs

---

## Golden Rule

Never rebase a shared or public branch.

Only rebase:

- Personal branches
- Local feature branches

---

# Merge vs Rebase

| Merge | Rebase |
|--------|---------|
| Preserves history | Rewrites history |
| Creates merge commits | Creates linear history |
| Safe for teams | Safe only locally |
| Recommended for shared branches | Recommended before merging |

---

# Git Clean

## What is Git Clean?

Git Clean removes untracked files from your project.

---

## Dry Run

```bash
git clean -n
```

Displays files that would be deleted.

Nothing is removed.

---

## Delete Files

```bash
git clean -f
```

Deletes all untracked files.

⚠️ This action cannot be undone.

---

# Git Tags

## What are Tags?

Tags mark important commits such as releases.

Instead of remembering commit IDs:

```
4d8f7bca98
```

You can use:

```
v1.0
v2.0
v3.1
```

---

## Create an Annotated Tag

```bash
git tag -a v1.0 -m "Release Version 1.0"
```

---

## View Tags

```bash
git tag
```

---

## View Tag Details

```bash
git show v1.0
```

---

## Push Tags

```bash
git push origin --tags
```

GitHub automatically displays pushed tags under the **Releases** section.

---

# Hands-on Practice

## Stash

```bash
git stash
git stash list
git stash pop
```

---

## Restore

```bash
git restore app.txt
git restore --staged app.txt
```

---

## Reset

```bash
git reset --soft HEAD~1
git reset --hard HEAD~1
```

---

## Revert

```bash
git revert HEAD
```

---

## Rebase

```bash
git checkout feature-login
git rebase main
```

---

## Clean

```bash
git clean -n
git clean -f
```

---

## Tag

```bash
git tag -a v1.0 -m "First Release"
git push origin --tags
```

---

# Common Advanced Commands

| Command | Purpose |
|----------|----------|
| `git stash` | Save unfinished work temporarily |
| `git stash pop` | Restore and remove stash |
| `git stash apply` | Restore while keeping stash |
| `git restore` | Discard local changes |
| `git restore --staged` | Unstage files |
| `git reset --soft` | Remove commit, keep staged changes |
| `git reset --hard` | Remove commit and discard all changes |
| `git revert` | Safely undo a commit with a new commit |
| `git merge` | Combine branches |
| `git rebase` | Rewrite history with a linear commit sequence |
| `git clean -n` | Preview untracked files for deletion |
| `git clean -f` | Delete untracked files |
| `git tag` | Create or list tags |
| `git push origin --tags` | Push tags to GitHub |

---

# Interview Questions

### What is the difference between `git reset` and `git revert`?

- `git reset` rewrites history by moving the branch pointer to an earlier commit. It is intended for private or local branches.
- `git revert` preserves history by creating a new commit that reverses the changes from a previous commit. It is the recommended approach for shared or public branches.

---

### When would you use `git stash`?

Use `git stash` when you have unfinished work that should not be committed yet, but you need to switch branches or work on another task.

---

### What is the difference between `git stash pop` and `git stash apply`?

- `git stash pop` restores the latest stash and removes it from the stash list.
- `git stash apply` restores the stash but keeps it in the stash list for future use.

---

### When should you use `git rebase` instead of `git merge`?

Use `git rebase` on local feature branches to create a clean, linear history before merging. Avoid rebasing branches that are already shared with others.

---

### What is the purpose of Git Tags?

Tags are used to mark significant commits, such as software releases (e.g., `v1.0`, `v2.0`), making them easy to identify and reference later.

---

# Summary

| Concept | Description |
|----------|-------------|
| Git Stash | Temporarily saves unfinished work |
| Git Restore | Discards or unstages local changes |
| Git Reset | Rewrites history by moving the branch pointer |
| Git Revert | Safely undoes a commit with a new commit |
| Git Merge | Combines branches while preserving history |
| Git Rebase | Rewrites history into a linear sequence |
| Git Clean | Removes untracked files |
| Git Tags | Marks important commits such as releases |