
import os
import shutil
import logging
from pathlib import Path

EXTENSIONS = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".py": "Code",
    ".c": "Code",
    ".cpp": "Code",
    ".java": "Code",
    ".js": "Code",
}

def unique_path(destination):
    """Generate a unique destination name without overwriting files."""
    if not destination.exists():
        return destination

    counter = 1
    while True:
        new_path = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        if not new_path.exists():
            return new_path
        counter += 1


def organize_folder(folder):
    """Organize files by extension and report the results."""
    folder = Path(folder).expanduser().resolve()

    if not folder.is_dir():
        print("Error: The folder does not exist.")
        return

    log_file = folder / "organizer.log"
    logging.basicConfig(
        filename=str(log_file),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True,
    )

    moved = 0
    skipped = 0
    errors = 0

    # Create category folders.
    for category in set(EXTENSIONS.values()):
        try:
            (folder / category).mkdir(exist_ok=True)
        except (PermissionError, OSError) as error:
            logging.error("Cannot create %s: %s", category, error)
            print(f"Cannot create folder {category}: {error}")
            errors += 1

    # Collect files from the selected folder only.
    try:
        with os.scandir(folder) as entries:
            files = [
                Path(entry.path)
                for entry in entries
                if entry.is_file(follow_symlinks=False)
                and entry.name != "organizer.log"
            ]
    except (PermissionError, OSError) as error:
        logging.error("Cannot read folder: %s", error)
        print(f"Error reading folder: {error}")
        return

    for file_path in files:
        category = EXTENSIONS.get(file_path.suffix.lower())

        if category is None:
            skipped += 1
            logging.info("Skipped unknown file type: %s", file_path.name)
            continue

        destination_folder = folder / category

        if not destination_folder.is_dir():
            errors += 1
            continue

        destination = unique_path(destination_folder / file_path.name)

        try:
            shutil.move(str(file_path), str(destination))
            moved += 1
            logging.info("Moved %s to %s", file_path.name, destination)
            print(f"Moved: {file_path.name} -> {category}/{destination.name}")
        except (PermissionError, FileExistsError, OSError) as error:
            errors += 1
            logging.error("Failed to move %s: %s", file_path.name, error)
            print(f"Could not move {file_path.name}: {error}")

    logging.info(
        "Summary: moved=%d, skipped=%d, errors=%d",
        moved, skipped, errors
    )

    print("\n========== ORGANIZER SUMMARY ==========")
    print(f"Files moved: {moved}")
    print(f"Files skipped: {skipped}")
    print(f"Errors: {errors}")
    print(f"Log file: {log_file}")
    print("=======================================")


if __name__ == "__main__":
    test_folder = input("Enter the folder path to organize: ").strip().strip('"')
    if test_folder:
        organize_folder(test_folder)
    else:
        print("No folder path entered.")
