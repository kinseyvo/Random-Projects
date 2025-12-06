import os
import hashlib

def get_file_hash(file_path):
  """Generate the MD5 hash of a file"""
  hash_md5 = hashlib.md5()
  with open(file_path, 'rb') as f:
    # Read the file in chunks to handle large files
    for chunk in iter(lambda: f.read(4096), b""):
      hash_md5.update(chunk)
  return hash_md5.hexdigest()

def find_duplicates(directory):
  """Find and print duplicate files in a directory"""
  # Dictionary to store file hashes
  hashes = {}
  duplicates = []

  # Walk through the directory
  for root, dirs, files in os.walk(directory):
    for file in files:
      file_path = os.path.join(root, file)
      file_hash = get_file_hash(file_path)

      # Check if this hash already exists in the dictionary
      if file_hash in hashes:
        duplicates.append((file_path, hashes[file_hash]))
      else:
        hashes[file_hash] = file_path

  return duplicates

def print_duplicates(duplicates):
  """Print the list of duplicates"""
  if not duplicates:
    print("No duplicates found.")
    return

  print("Duplicate files found:")
  for file1, file2 in duplicates:
    print(f"Duplicate: {file1} <=> {file2}")

def main():
  # Ask the user for a directory
  directory = input("Enter the directory to search for duplicates: ").strip()

  if not os.path.isdir(directory):
    print(f"The directory {directory} does not exist.")
    return

  # Find duplicates in the directory
  duplicates = find_duplicates(directory)

  # Print duplicates
  print_duplicates(duplicates)

if __name__ == "__main__":
  main()
