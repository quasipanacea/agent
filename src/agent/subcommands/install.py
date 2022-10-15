import os
from pathlib import Path


# task.symlink() {
# 	local file="dev.kofler.kaxon.native.json"
# 	for browser_path in 'BraveSoftware/Brave-Browser' 'microsoft-edge'; do
# 		ln -Tfs "$PWD/$file" "${XDG_CONFIG_HOME:-$HOME/.config}/$browser_path/NativeMessagingHosts/$file"
# 	done
# }

def get_xdg_data_dir() -> Path:
    if "XDG_DATA_HOME" in os.environ:
        xdgDataHome = os.environ.get("XDG_DATA_HOME")

        if len(xdgDataHome) > 0 and xdgDataHome[:1] == "/":
            return Path(xdgDataHome)

    return Path.home() / ".local" / "share"


applicationsDir = get_xdg_data_dir() / "applications"

# Update the cache
mimeInfoCachePath = applicationsDir / "mimeinfo.cache"
mimeInfoCacheText = mimeInfoCachePath.read_text()
scheme = "x-scheme-handler/kaxon=kaxon.desktop;\n"
if not scheme in mimeInfoCacheText:
    with open(mimeInfoCachePath, "a") as f:
        f.write(scheme)

# Update the desktop file
src = Path(os.path.abspath(__file__)).parent / "kaxon.desktop"
dest = applicationsDir / "kaxon.desktop"
os.symlink(src, dest, target_is_directory=False)

# Update the PATH
bashrcPath = Path.home() / ".bashrc"
bashrcText = bashrcPath.read_text()
scheme = f'PATH="${Path.cwd()}/bin:$PATH"\n'
if not scheme in bashrcText:
    with open(bashrcPath, "a") as f:
        f.write(scheme)
