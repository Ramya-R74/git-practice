# Git Branching and Merging

## What is Branching?

Branching is one of Git's most powerful features. It allows developers to work on new features, bug fixes, or experiments without affecting the main codebase.

A branch is an independent line of development that starts as an exact copy of another branch.

### Why use branches?

- Develop features independently
- Fix bugs safely
- Experiment without affecting production code
- Enable multiple developers to work simultaneously
- Simplify collaboration

---

# How Branching Works

```
             main
              │
              ●
              │
        git branch feature-login
              │
      ┌───────┘
      ▼
feature-login
      │
      ●
      │
      ●
```

The new branch begins from the current commit of the parent branch.

---

# Viewing Branches

List all local branches:

```bash
git branch
```

Example:

```text
* main
  feature-login
  bugfix-navbar
```

The `*` indicates the currently active branch.

---

# Create a Branch

Create a new branch:

```bash
git branch feature-login
```

This creates the branch but does not switch to it.

---

# Switch to a Branch

```bash
git checkout feature-login
```

Git updates your working directory to match the selected branch.

> **Note:** Any uncommitted changes must be committed or stashed before switching branches.

---

# Create and Switch in One Command

```bash
git checkout -b feature-login
```

This command:

- Creates the branch
- Switches to it immediately

---

# View Branch History

A simple graph of all branches:

```bash
git log --oneline --graph --all
```

Example:

```text
* 5b12f8a Add login page
|\
| * 81a4de2 Create login form
|/
* a38d5f0 Initial commit
```

---

# Merging Branches

After completing work on a feature branch, merge it into the target branch.

## Step 1

Switch to the receiving branch.

```bash
git checkout main
```

---

## Step 2

Merge the feature branch.

```bash
git merge feature-login
```

Git combines the history of both branches.

---

# Fast-Forward Merge

If no changes exist on the target branch after creating the feature branch, Git performs a **Fast-Forward Merge**.

```
Before

main
  │
  ●
   \
feature
    ●
    ●

After

main
  │
  ●──●──●
```

No extra merge commit is created.

---

# Three-Way Merge

If both branches contain new commits, Git creates a merge commit.

```
        ● feature
       /
●──●──●
       \
        ● main

After Merge

        ●
       / \
●──●──●──●
```

---

# Merge Conflicts

A merge conflict occurs when Git cannot automatically combine changes because the same section of a file has been modified differently in two branches.

Git pauses the merge and asks you to resolve the conflict manually.

---

# Conflict Markers

Git inserts conflict markers into the affected file.

```text
<<<<<<< HEAD
This is the code from the current branch.
=======
This is the code from the incoming branch.
>>>>>>> feature-login
```

### Meaning of the markers

| Marker | Meaning |
|---------|----------|
| `<<<<<<< HEAD` | Beginning of the current branch's changes |
| `=======` | Separator between both versions |
| `>>>>>>> feature-login` | End of incoming branch changes |

---

# Resolving a Merge Conflict

### Step 1

Open the conflicted file.

Example:

```text
<<<<<<< HEAD
Hello World
=======
Hello Git
>>>>>>> feature-login
```

---

### Step 2

Choose the desired content.

Example:

```text
Hello World and Git
```

Delete all conflict markers.

---

### Step 3

Save the file.

---

### Step 4

Stage the resolved file.

```bash
git add app.txt
```

---

### Step 5

Complete the merge.

```bash
git commit
```

Git creates a merge commit.

---

# Hands-on Practice

## Step 1

Create a repository.

```bash
mkdir git-branch-practice
cd git-branch-practice
git init
```

---

## Step 2

Create a file.

```bash
echo "Hello World" > app.txt
```

Commit it.

```bash
git add .
git commit -m "Initial commit"
```

---

## Step 3

Create and switch to a feature branch.

```bash
git checkout -b feature-a
```

---

## Step 4

Modify the file.

```text
Hello from Feature A
```

Commit the changes.

```bash
git add .
git commit -m "Update from feature branch"
```

---

## Step 5

Switch back to main.

```bash
git checkout main
```

---

## Step 6

Modify the same line.

```text
Hello from Main
```

Commit the change.

```bash
git add .
git commit -m "Update from main"
```

---

## Step 7

Merge the feature branch.

```bash
git merge feature-a
```

Git reports a merge conflict.

---

## Step 8

Open `app.txt`.

Resolve the conflict by editing the file and removing the conflict markers.

---

## Step 9

Stage the resolved file.

```bash
git add app.txt
```

---

## Step 10

Complete the merge.

```bash
git commit
```

---

# Common Branch Commands

| Command | Purpose |
|----------|----------|
| `git branch` | List local branches |
| `git branch <name>` | Create a branch |
| `git checkout <branch>` | Switch branches |
| `git checkout -b <name>` | Create and switch |
| `git merge <branch>` | Merge a branch |
| `git log --graph --all --oneline` | View branch graph |
| `git branch -d <branch>` | Delete a merged branch |
| `git branch -D <branch>` | Force delete a branch |

---

# Interview Questions

### Why do we use branches?

To isolate development work, prevent breaking the main codebase, and enable parallel collaboration.

---

### What is the difference between `git branch` and `git checkout`?

- `git branch` creates or lists branches.
- `git checkout` switches your working directory to another branch.

---

### What causes a merge conflict?

A merge conflict occurs when the same part of a file has been modified differently in two branches, preventing Git from merging automatically.

---

### What is the difference between a Fast-Forward Merge and a Three-Way Merge?

- **Fast-Forward Merge:** No new merge commit is created because the target branch has not diverged.
- **Three-Way Merge:** Git creates a merge commit because both branches have new commits.

---

# Summary

| Concept | Description |
|----------|-------------|
| Branch | Independent line of development |
| Checkout | Switch to another branch |
| Merge | Combine changes from one branch into another |
| Merge Conflict | Git cannot automatically combine changes |
| Conflict Markers | Indicators showing conflicting code sections |