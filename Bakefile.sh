# shellcheck shell=bash

task.symlink() {
	local file="dev.kofler.kaxon.native.json"
	for browser_path in 'BraveSoftware/Brave-Browser' 'microsoft-edge'; do
		ln -Tfs "$PWD/$file" "${XDG_CONFIG_HOME:-$HOME/.config}/$browser_path/NativeMessagingHosts/$file"
	done
}
