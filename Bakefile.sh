# shellcheck shell=bash

task.init() {
	poetry install
}

task.release-nightly() {
	mkdir -p './output'

	# Build
	poetry bundle venv './build' --clear
	tar czf './build.tar.gz' './build'
	mv './build.tar.gz' './output'

	util.publish './output/build.tar.gz'
}

util.publish() {
	local file="$1"
	bake.assert_not_empty 'file'

	local tag_name='nightly'
	git tag -fa "$tag_name" -m ''
	git push origin ":refs/tags/$tag_name"
	git push --tags
	gh release upload "$tag_name" "$file" --clobber
	gh release edit --draft=false nightly
}
