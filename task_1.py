import shutil
import argparse
from pathlib import Path

DEFAULT_DESTINATION_DIR = "dist"

def copy_and_sort_files(source_dir: Path, dest_dir: Path):
    """Copies all files from source_dir to dest_dir and sorts them by name."""

    try:
        for element in source_dir.iterdir():
            if element.is_dir():
                if element.resolve() != dest_dir.resolve():
                    copy_and_sort_files(element, dest_dir)
                continue
            elif element.is_file():
                extension = element.suffix.lstrip('.').lower() or "no_extension"
                target_subdir = dest_dir / extension
                target_subdir.mkdir(parents=True, exist_ok=True)
                target_file = target_subdir / element.name

                try:
                    shutil.copy2(element, target_file)
                    print(f"Copied: {element.name} -> {target_subdir.name}")
                except OSError as e:
                    print(f"Failed to copy {element.name}: {e}")
    
    except PermissionError as e:
        print(f"Permission denied while accessing {source_dir}: {e}")
    except Exception as e:
        print(f"An error occurred while processing {source_dir}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Copy and sort files by extension.")
    parser.add_argument("source", type=Path, help="Source directory to copy files from.")
    parser.add_argument("--dest", type=Path, default=Path(DEFAULT_DESTINATION_DIR), help="Destination directory to copy files to.")
    args = parser.parse_args()

    source_path = Path(args.source)
    dest_path = Path(args.dest)

    if not source_path.is_dir():
        print(f"The source path '{source_path}' is not a valid directory.")
        return
    
    try:
        dest_path.mkdir(parents=True, exist_ok=True)
        print(f"\nDestination directory '{dest_path}' is ready.")
    except OSError as e:
        print(f"Failed to create destination directory '{dest_path}': {e}")
        return
    
    print("\nStarting file copy and sort process...")
    copy_and_sort_files(source_path, dest_path)
    print("\nFile copy and sort process completed.")

if __name__ == "__main__":
    main()
