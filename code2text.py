'''
Convert code files (*.py) to text files (*.py.txt)
Why? idk
Run python file from it's local dir
'''

import os
import glob

DIRS_PREFIX: str = "MDP_"
'''Search and perform operations inside this dir only'''

VALID_FILE_EXTS: set = {
    ".c", ".h", ".s",       # STM32
    ".cpp", ".hpp",         # STM32
    ".java",                # android, algorithm code
    ".py",                  # pi and image recog
    ".sh"                   # pi, probably
}

def append_to_file(file_path: str):
    os.rename(file_path, f"{file_path}.txt")

def recursive_code_to_text(dir_path: str):
    '''Recursively append ".txt" to all applicable files'''

    discovered_paths = glob.glob(f"{dir_path}/*") ## contains both files and dirs
    print(f"discovered paths {discovered_paths}")

    for _path in discovered_paths:
        if os.path.isfile(_path) and os.path.splitext(_path)[-1] in VALID_FILE_EXTS:
            print(f"modifying file {_path}...")
            append_to_file(_path)


    discovered_dirs: list = glob.glob(f"{dir_path}/*/") # get all dirs
    print(f"recursing {discovered_dirs}")

    ## recurse
    for _path in discovered_dirs:
        recursive_code_to_text(f"{_path}")


def main():
    head_directories: list = glob.glob(f"{DIRS_PREFIX}*")

    for dir in head_directories:
        recursive_code_to_text(dir)

    return


if __name__ == "__main__":
    main()
