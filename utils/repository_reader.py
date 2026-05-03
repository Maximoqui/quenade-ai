from pathlib import Path


IGNORED_DIRS = {
    ".git",
    "__pycache__",
    "venv",
    ".venv",
    "node_modules"
}


ALLOWED_EXTENSIONS = {
    ".py",
    ".c",
    ".cpp",
    ".h",
    ".java",
    ".js"
}


def get_files(path_str):

    path = Path(path_str)


    if path.is_file():

        return [path]


    if path.is_dir():

        files = []


        for file in path.rglob("*"):

            if not file.is_file():
                continue


            if any(part in IGNORED_DIRS for part in file.parts):
                continue


            if file.suffix not in ALLOWED_EXTENSIONS:
                continue


            files.append(file)


        return files


    raise Exception("Path not found")