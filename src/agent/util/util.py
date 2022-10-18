from genericpath import isdir
import os
from pathlib import Path

def get_xdg_data_dir() -> Path:
    if "XDG_DATA_HOME" in os.environ:
        xdgDataHome = os.environ.get("XDG_DATA_HOME")

        if len(xdgDataHome) > 0 and xdgDataHome[:1] == "/":
            return Path(xdgDataHome)

    return Path.home() / ".local" / "share"

def get_bin_dir():
    return Path.home() / '.local' / 'bin'

def get_workspace_dir():
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    # HACK: if not in development (that is, on the nightly releases), the built files will be inside the 'build' directory, under even more
    # subdirectories, throwing everything off. So account for this
    if os.path.basename(root) != 'repos':
        root = os.path.dirname(os.path.dirname(os.path.dirname(root)))

    return root

def get_dir_in_workspace(repo_name: str):
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    # HACK: if not in development (that is, on the nightly releases), the built files will be inside the 'build' directory, under even more
    # subdirectories, throwing everything off. So account for this
    if os.path.basename(root) != 'repos':
        root = os.path.dirname(os.path.dirname(os.path.dirname(root)))

    repo_dir = os.path.join(root, repo_name)

    if not os.path.isdir(repo_dir):
        raise Exception(f'Not a directory: {repo_dir}')

    return repo_dir

def download_and_cd_nightly_artifact(repo_name: str):
    workspace_dir = get_workspace_dir()
    print(workspace_dir)
    # os.system(f"curl -#SfLo \"{repo_name}.tar.gz\" \"https://github.com/project-kaxon/{repo_name}/releases/download/nightly/build.tar.gz\"")
