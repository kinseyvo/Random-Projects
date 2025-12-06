# File Duplicate Finder
## Overview
The File Duplicate Finder is a simple Python tool that scans a specified directory for duplicate files based on their content (not just file names). It uses hash functions to compare files, ensuring that files with identical content are identified, even if they have different names.

This tool is useful for cleaning up your filesystem and reclaiming storage space by detecting and removing duplicate files.

## Features
- Scans a directory (and subdirectories) for duplicate files
- Compares files based on their content (MD5 hash)
- Lists duplicate files with their paths
- Easy to run via the command line

## Requirements
- Python 3.x
- No external libraries are required, only Python’s built-in ```os``` and ```hashlib``` modules

## How to Run
1. Clone or Download the Repository:

    ```git clone https://github.com/yourusername/file-duplicate-finder.git```

2. Navigate to the Project Folder:
- Open a terminal or command prompt and change to the directory containing the duplicate_finder.py script.

    ```cd /path/to/your/project/folder```

3. Run the Script:

    ```python duplicate_finder.py```

4. Enter Directory Path:
- The program will prompt you to enter the path of the directory you want to scan for duplicate files.
- Example:

    ```Enter the directory to search for duplicates: /path/to/scan```
- The script will then begin scanning the directory and will display any duplicate files it finds.

## How It Works
1. **Directory Scanning:** The script recursively walks through the specified directory and collects all the file paths.
2. **File Hashing:** For each file, the script generates an MD5 hash to identify the content of the file.
3. **Duplicate Detection:** If two files share the same hash, they are flagged as duplicates and listed.
4. **Results:** The duplicates are displayed in the terminal, showing the paths of the duplicate files.

## Example Output

```Enter the directory to search for duplicates: /Users/john/Downloads```

```Duplicate files found:```

```Duplicate: /Users/john/Downloads/photo1.jpg <=> /Users/john/Downloads/photo1_copy.jpg```

```Duplicate: /Users/john/Downloads/music.mp3 <=> /Users/john/Downloads/music_copy.mp3```
