from genericpath import isdir
import os
from pathlib import Path
import shutil

def get_xdg_config_dir() -> Path:
    if "XDG_CONFIG_HOME" in os.environ:
        xdg_config_home = os.environ.get("XDG_CONFIG_HOME")

        if len(xdg_config_home) > 0 and xdg_config_home[:1] == "/":
            return Path(xdg_config_home)

    return Path.home() / ".config"

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
    init_dir = Path(get_workspace_dir()).parent
    os.chdir(init_dir)

    os.makedirs('nightly', exist_ok=True)
    os.chdir('nightly')

    os.remove(f'{repo_name}.tar.gz')
    shutil.rmtree('./build')

    os.system(f"curl -#SfLo \"{repo_name}.tar.gz\" \"https://github.com/cosmic-knowledge/{repo_name}/releases/download/nightly/build.tar.gz\"")
    os.system(f'tar xf ./{repo_name}.tar.gz')

def must_either_dev_or_nightly(dev: bool, nightly: bool):
    if (not dev and not nightly):
        print("Must pass at least --dev or --nightly, or both")
        exit(1)

def install_native_json_manifest(content: str):
    xdg_config_dir = get_xdg_config_dir()

    file_name = 'dev.kofler.quazipanacea.native.json'
    for browser_name in ["BraveSoftware/Brave-Browser", "BraveSoftware/Brave-Browser-Beta", "BraveSoftware/Brave-Browser-Nightly", "microsoft-edge", "microsoft-edge-beta", "microsoft-edge-dev"]:
        manifest_file = Path(xdg_config_dir) / browser_name / "NativeMessagingHosts" / file_name
        manifest_file.parent.mkdir(0o755, True, exist_ok=True)

        if os.path.exists(manifest_file):
            os.remove(manifest_file)
        manifest_file.write_text(content)
