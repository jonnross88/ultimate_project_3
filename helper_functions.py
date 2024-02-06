"""Python file with helper funtions for notebook"""

from pathlib import Path
from zipfile import ZipFile, is_zipfile


# Check if the zipfile exists with a function
def check_zipfile(zip_path: Path) -> bool:
    """Check if the zipfile exists at the given path."""
    return zip_path.exists() and is_zipfile(zip_path)


# Create a function to create a new directory
def create_target_directory(target_dir: Path):
    """Creates a new_directory and returns it."""
    target_dir.mkdir(parents=True, exist_ok=True)
    return target_dir


def extract_zipfile(zip_path: Path, target_dir: Path):
    """Extracts the contents of zip at zip_path to target_dir."""
    with ZipFile(zip_path, "r") as zip_ref:
        # get a list of all the files in the zipfile
        for file in zip_ref.namelist():
            # if the file does not exist in the target directory, extract it
            if not (target_dir / file).exists():
                zip_ref.extract(file, target_dir)
        print(f"Extracted {zip_path} to {target_dir}")
