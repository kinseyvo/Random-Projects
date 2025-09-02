import os, shutil, argparse, time

def should_copy(src_file, dst_file):
    if not os.path.exists(dst_file):
        return True
    return os.path.getmtime(src_file) > os.path.getmtime(dst_file)

def sync_dirs(src, dst, dry_run=False):
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    for root, _, files in os.walk(src):
        rel_path = os.path.relpath(root, src)
        dst_root = os.path.join(dst, rel_path)
        if not os.path.exists(dst_root):
            os.makedirs(dst_root)
    
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dst_root, file)

            if should_copy(src_file, dst_file):
                print(f"{'Would copy' if dry_run else 'Copying'}: {src_file} -> {dst_file}")
                if not dry_run:
                    shutil.copy2(src_file, dst_file)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True, help="Source directory")
    parser.add_argument("--dst", required=True, help="Destination directory")
    parser.add_argument("--dry-run", action="store_true", help="Preview files that would be copied")

    args = parser.parse_args()
    sync_dirs(args.src, args.dst, args.dry_run)

if __name__ == "__main__":
    main()