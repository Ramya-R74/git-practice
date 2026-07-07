# Git Basics

## What is Git?

Git is a distributed version control system that tracks every change made to your project files. It records:

- What changed
- When it changed
- Who changed it
- Where the change occurred

Git enables developers to collaborate efficiently while maintaining a complete history of the project.

---

# Local Git Architecture

Every local Git repository consists of three important areas.

```
Working Directory
        │
        ▼
 Staging Area (Index)
        │
        ▼
 Local Repository (.git)
```

## 1. Working Directory

The Working Directory is your project folder where you create and edit files.

Examples:

- Create files
- Modify files
- Delete files

This is your active workspace.

---

## 2. Staging Area (Index)

The Staging Area acts as a temporary checkpoint before saving changes permanently.

It allows you to:

- Review changes
- Select only required files
- Prepare commits

Think of it as a "shopping cart" before checkout.

---

## 3. Local Repository

After staging your changes, Git stores them permanently inside the hidden `.git` folder.

Every commit becomes part of the project's history.

---

# Git Workflow

```
Create/Edit File
       │
       ▼
Working Directory
       │
git add
       ▼
Staging Area
       │
git commit
       ▼
Local Repository
```

---

# Initialize a Repository

Create a Git repository inside any folder.

```bash
git init
```

Git creates a hidden folder called:

```
.git
```

This folder stores all Git history and metadata.

---

# Configure Git Identity

Configure your username:

```bash
git config --global user.name "Your Name"
```

Configure your email:

```bash
git config --global user.email "your.email@example.com"
```

### Global Configuration

Applies to every repository on your computer.

### Local Configuration

```bash
git config --local user.name "Your Name"
git config --local user.email "your@email.com"
```

Applies only to the current repository.

---

# Check Repository Status

```bash
git status
```

Displays:

- Modified files
- Deleted files
- New files
- Staged files
- Current branch

This is one of the most frequently used Git commands.

---

# View File Changes

```bash
git diff
```

Shows line-by-line differences between your current files and the last committed version.

---

# Staging Files

## Stage One File

```bash
git add index.html
```

Stages only the specified file.

---

## Stage Current Folder

```bash
git add .
```

Stages:

- New files
- Modified files
- Deleted files

Only inside the current directory and its subdirectories.

---

## Stage Entire Repository

```bash
git add -A
```

Stages every change in the repository.

Includes:

- New files
- Modified files
- Deleted files

---

## Stage Using Wildcard

```bash
git add *
```

Stages:

- New visible files
- Modified files

Does **not** stage deleted files.

---

# Commit Changes

```bash
git commit -m "Initial commit"
```

The `-m` option allows you to write a meaningful commit message.

Good commit messages describe **what changed**, not **how**.

Example:

```text
Add login page

Fix navigation bug

Update README

Create Git practice project
```

---

# View Commit History

Full history:

```bash
git log
```

Compact history:

```bash
git log --oneline
```

Example:

```
8b31f5d Initial commit

4cd12f8 Add login page

a52c987 Fix footer
```

---

# Ignore Files

Create a file named:

```
.gitignore
```

Example:

```text
*.log
node_modules/
.env
secrets.json
```

Git will ignore these files.

Commonly ignored:

- Password files
- Environment variables
- Build folders
- Temporary files
- Logs

---

# Practice Exercise

## Step 1

Create a project.

```bash
mkdir git-practice
cd git-practice
```

---

## Step 2

Initialize Git.

```bash
git init
```

Verify the hidden `.git` folder.

Linux/macOS:

```bash
ls -la
```

Windows PowerShell:

```powershell
dir -Force
```

---

## Step 3

Create a file.

Example:

```
index.html
```

---

## Step 4

Check status.

```bash
git status
```

Output:

```
Untracked files:
index.html
```

---

## Step 5

Stage the file.

```bash
git add index.html
```

Run:

```bash
git status
```

The file now appears under:

```
Changes to be committed
```

---

## Step 6

Commit.

```bash
git commit -m "Initial commit"
```

---

## Step 7

View history.

```bash
git log --oneline
```

Example:

```
f13b234 Initial commit
```

---

# Summary

| Area | Purpose |
|-------|----------|
| Working Directory | Where you edit files |
| Staging Area | Prepare changes before committing |
| Local Repository | Permanent Git history |

---

# Frequently Used Commands

| Command | Purpose |
|----------|----------|
| `git init` | Initialize repository |
| `git status` | Check repository status |
| `git diff` | View changes |
| `git add file` | Stage one file |
| `git add .` | Stage current directory |
| `git add -A` | Stage entire repository |
| `git commit -m` | Save changes |
| `git log` | View history |
| `git log --oneline` | Compact history |
| `git config` | Configure Git |