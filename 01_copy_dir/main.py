import sys
from pathlib import Path
from dir_ops import copy_dir

def main():
    try:
        if len(sys.argv) > 1:
            _, from_dir, *args = sys.argv
            root_dir = Path(from_dir)
            dist_dir = Path(args[0]) if len(args) else Path.cwd()/'dist'
            if (not root_dir.exists() or not root_dir.is_dir()):
                print("Not directory or does not exitsts")
                return
            copy_dir(root_dir, dist_dir)
    except Exception as e:
        print("Some error occured", e)

if __name__ == "__main__":
    main()
