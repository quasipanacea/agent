import argparse
import sys
from agent import subcommands


def run():
    parser = argparse.ArgumentParser(description="Run the Kaxon agent")
    subparsers = parser.add_subparsers(required=True, dest="subcommand")

    parser_buildall = subparsers.add_parser('app-build')
    parser_install = subparsers.add_parser("app-install")
    parser_uninstall = subparsers.add_parser("app-uninstall")

    parser_launcher = subparsers.add_parser("launch")
    parser_webext_native_client = subparsers.add_parser("webext-native-client")

    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)

    args = parser.parse_args()
    if args.subcommand == 'app-build':
        subcommands.build()
    elif args.subcommand == "app-install":
        # subcommands.install('dev')
        subcommands.install('nightly')
    elif args.subcommadn == "app-uninstall":
        subcommands.uninstall('dev')
        subcommands.install('nightly')
    elif args.subcommand.launch() == "launch":
        subcommands.launch()
    elif args.subcommand == "webext-native-client":
        subcommands.webext_native_client()
    else:
        print("Subcommand not found")
        exit(1)
