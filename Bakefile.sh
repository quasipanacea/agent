# shellcheck shell=bash

task.symlink() {
	local file="dev.kofler.kaxon.native.json"
	ln -Tfs "$PWD/$file" "${XDG_CONFIG_HOME:-$HOME/.config}/BraveSoftware/Brave-Browser/NativeMessagingHosts/$file" 
}