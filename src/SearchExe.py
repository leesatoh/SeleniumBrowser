import glob
import string
from os.path import expanduser


def search(search_path) -> string:
    for name in glob.glob(search_path, recursive=True):
        print(name)
        return name.replace("\\", "/")
    return None


def do_search(hint, exe_name):
    # local
    print("local check")
    search_path = f'./**/{exe_name}'
    exe_path = search(search_path)
    if exe_path is not None:
        return exe_path

    # home App
    home_dir = expanduser("~").replace("\\", "/")
    print("home check")
    # TODO:windows前提だけどLinuxも考える必要あり？os.path.join使っていい感じに？
    search_path = f'{home_dir}/AppData/Local/{hint}/**/{exe_name}'
    exe_path = search(search_path)
    if exe_path is not None:
        return exe_path

    # program
    home_dir = expanduser("~")
    print("no quote hint")
    # TODO:windows前提だけどLinuxも考える必要あり？
    search_path = f'C:/Program Files/{hint}/**/{exe_name}'
    exe_path = search(search_path)
    if exe_path is not None:
        return exe_path

    # program
    home_dir = expanduser("~")
    print("no quote hint 86")
    # TODO:windows前提だけどLinuxも考える必要あり？
    search_path = f'C:/Program Files (x86)/{hint}/**/{exe_name}'
    exe_path = search(search_path)
    if exe_path is not None:
        return exe_path


    # program
    home_dir = expanduser("~")
    print("quote hint")
    # TODO:windows前提だけどLinuxも考える必要あり？
    search_path = f'C:/"Program Files"/{hint}/**/{exe_name}'
    exe_path = search(search_path)
    if exe_path is not None:
        return exe_path

    # program
    home_dir = expanduser("~")
    print("quote hint 86")
    # TODO:windows前提だけどLinuxも考える必要あり？
    search_path = f'C:/"Program Files (x86)"/{hint}/**/{exe_name}'
    exe_path = search(search_path)
    if exe_path is not None:
        return exe_path

    # program
    home_dir = expanduser("~")
    print("no quote")
    # TODO:windows前提だけどLinuxも考える必要あり？
    search_path = f'C:/Program Files/**/{exe_name}'
    exe_path = search(search_path)
    if exe_path is not None:
        return exe_path

    # program
    home_dir = expanduser("~")
    print("no quote 86")
    # TODO:windows前提だけどLinuxも考える必要あり？
    search_path = f'C:/Program Files (x86)/**/{exe_name}'
    exe_path = search(search_path)
    if exe_path is not None:
        return exe_path
