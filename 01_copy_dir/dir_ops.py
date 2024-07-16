from pathlib import Path
from shutil import copy2

def copy_dir(from_dir: Path, dist_dir: Path):
    try:
        dist_dir.mkdir(parents=True, exist_ok=True)
        for path in from_dir.iterdir():
            if (path.is_dir()):
                copy_dir(path, dist_dir/path.name)
            elif (path.is_file()):
                ext = path.suffix[1:]
                ext_dir = dist_dir/ext
                ext_dir.mkdir(parents=True, exist_ok=True)
                copy2(path, ext_dir)
            else:
                print(f"In {from_dir.name} Unknown entity: {path.name}")
    except Exception as e:
        print("Error while file/directory operation", e)
