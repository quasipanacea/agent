import os
from pathlib import Path
import pathlib
from agent import util
from jinja2 import Environment, Template

def app_install(dev: bool, nightly: bool):
    if dev:
        install_aggregator('dev')
        install_agent('dev')
        install_server('dev')
        install_webext('dev')
    if nightly:
        install_aggregator('nightly')
        install_agent('nightly')
        install_server('nightly')
        install_webext('nightly')
#     # Desktop files
#     applications_dir = util.get_xdg_data_dir() / 'applications'
#     os.makedirs(applications_dir, exist_ok=True)
#     file_input = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))) / 'share' / 'kaxon.desktop'
#     file_output = applications_dir / f'kaxon{postfix}.desktop'
#     template_input = Path(file_input).read_text()
#     template_output = Template(template_input).render(
#         tmpl_name=tmpl_name,
#         tmpl_exec=tmpl_exec
#     )
#     Path(file_output).write_text(template_output)

def install_aggregator(deploy_type: str) -> None:
    if deploy_type == '':
        postfix = ''
    else:
        postfix = '-' + deploy_type

    bin_dir = util.get_bin_dir()
    bin_file = Path(os.path.join(bin_dir, f'kaxon-aggregator{postfix}'))

    if deploy_type == 'dev':
        aggregator_dir = util.get_dir_in_workspace('aggregator')
        bin_file.write_text(f'''#!/usr/bin/env bash
set -e

readonly aggregator_dir="{aggregator_dir}"
exec "$aggregator_dir/build/aggregator" "$@"
''')
        os.chmod(bin_file, 0o755)

    elif deploy_type == 'nightly':
        util.download_and_cd_nightly_artifact('aggregator')
        bin_file.write_bytes(Path('./build/bin/aggregator').read_bytes())
        bin_file.chmod(0o755)
    else:
        raise Exception("Bad deploy_type")

def install_agent(deploy_type: str) -> None:
    if deploy_type == '':
        postfix = ''
    else:
        postfix = '-' + deploy_type

    bin_dir = util.get_bin_dir()
    bin_file = Path(os.path.join(bin_dir, f'kaxon-agent{postfix}'))
    agent_dir = util.get_dir_in_workspace('agent')

    if deploy_type == 'dev':
        bin_file.write_text(f'''#!/usr/bin/env bash
set -e

readonly agent_dir="{agent_dir}"
exec "$agent_dir/build/bin/agent" "$@"
''')
        os.chmod(bin_file, 0o755)
    elif deploy_type == 'nightly':
        pass
    else:
        raise Exception("Bad deploy_type")

def install_server(deploy_type: str):
    if deploy_type == '':
        postfix = ''
    else:
        postfix = '-' + deploy_type

    bin_dir = util.get_bin_dir()
    bin_file = Path(os.path.join(bin_dir, f'kaxon-server{postfix}'))
    server_dir = util.get_dir_in_workspace('server-deno')
    client_dir = util.get_dir_in_workspace('client-web')

    if deploy_type == 'dev':
        bin_file.write_text(f'''#!/usr/bin/env bash
set -e

readonly server_dir="{server_dir}"
readonly client_dir="{client_dir}"
KAXON_CLIENT_DIR=$client_dir exec deno run --allow-all "$server_dir/build/bundle.js" -- "$@"
''')
        os.chmod(bin_file, 0o755)
    elif deploy_type == 'nightly':
        raise Exception("shit, nightly?")
    else:
        raise Exception("Bad deploy_type")

def install_webext(deploy_type: str) -> None:
    if deploy_type == '':
        postfix = ''
    else:
        postfix = '-' + deploy_type

    bin_dir = util.get_bin_dir()
    bin_file = Path(os.path.join(bin_dir, f'kaxon-agent{postfix}'))
    agent_dir = util.get_dir_in_workspace('agent')

    workspace_dir = util.get_workspace_dir()
    kaxon_launch_bin = Path(workspace_dir) / 'agent/bin/kaxon-launch'
    if deploy_type == 'dev':
       util.install_native_json_manifest(f'''{{
	"name": "dev.kofler.kaxon.native",
	"description": "Kaxon native component for Brave extension",
	"path": "{kaxon_launch_bin}",
	"type": "stdio",
	"allowed_origins": ["chrome-extension://ahhfnedchjgnbplbclgfmhmgoeeecncn/"]
}}''')
    elif deploy_type == 'nightly':
        raise Exception("shit, nightly?")
    else:
        raise Exception("Bad deploy_type")
# def doTheThing():
#     # Update the cache
#     mimeInfoCachePath = applicationsDir / "mimeinfo.cache"
#     mimeInfoCacheText = mimeInfoCachePath.read_text()
#     scheme = "x-scheme-handler/kaxon=kaxon.desktop;\n"
#     if not scheme in mimeInfoCacheText:
#         with open(mimeInfoCachePath, "a") as f:
#             f.write(scheme)

#     # Update the desktop file
#     src = Path(os.path.abspath(__file__)).parent / "kaxon.desktop"
#     dest = applicationsDir / "kaxon.desktop"
#     os.symlink(src, dest, target_is_directory=False)
