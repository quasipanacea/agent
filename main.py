import argparse
import sys

parser = argparse.ArgumentParser(description='Run the Kaxon agent')
subparsers = parser.add_subparsers(required=True, dest='subcommand')

parser_install = subparsers.add_parser('install')
parser_launcher = subparsers.add_parser('launch')
parser_webext_native_client = subparsers.add_parser('webext-native-client')

if len(sys.argv) < 2:
    parser.print_usage()
    sys.exit(1)

args = parser.parse_args()
if args.subcommand == 'install':
    from src.subcommands.install import install
    install()
if args.subcommand == 'launch':
    from src.subcommands.launch import launch
    launch()
elif args.subcommand == 'webext-native-client':
    from src.subcommands.webext_native_client import webext_native_client
    webext_native_client()
