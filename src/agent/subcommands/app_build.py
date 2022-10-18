import os
from pathlib import Path
from typing import Callable
from agent import util

def app_build():
    cd('aggregator', build_aggregator)
    cd('agent', build_agent)
    cd('client-web', build_client_web)
    cd('server-deno', build_server_deno)
    cd('webext', build_webext)

def cd(dir: str, fn: Callable):
    repo_dir = Path(util.get_dir_in_workspace(dir))

    print('______________________________________________________________')
    print(f'BUILDING THE FOLLOWING DIRECTORY: {repo_dir.name}')
    print('______________________________________________________________')
    os.chdir(repo_dir)
    fn()
    os.chdir(repo_dir.parent)
    print('\n\n')

def build_aggregator():
    os.system('./bake build')

def build_agent():
    os.system('./bake build')

def build_client_web():
    os.system('./bake build')

def build_server_deno():
    os.system('./bake build')

def build_webext():
    os.system('./bake build')
