# Simple File Sync Tool
A lightweight Python utility to sync files from one directory to another. Only copies files that are **new or updated**, making it useful for quick backups or development folder syncing.

## Features
- Copies newer/modified files from source to destination
- Preserves directory structure
- Optional '--dry-run' mode to preview changes

## How It Works
- Walks the source directory recursively
- Compares file mtime (modified time) in source vs destination
- Copies file if:
    - It doesn't exist in destination
    - Source file is newer

## Requirements
- Python 3.x

## Usage
```
# Basic sync
python sync.py --src ./my_folder --dst ./my_backup

# Preview (dry-run) without copying
python sync.py --src ./my_folder --dst ./my_backup --dry-run
```

## Example
```
python sync.py --src ./project --dst ./backup --dry-run
```
- Would copy: project/index.html -> backup/index.html
- Would copy: project/assets/logo.png -> backup/assets/logo.png
