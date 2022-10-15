import argparse
import sys
import agent.subcommands


def run():
    parser = argparse.ArgumentParser(description="Run the Kaxon agent")
    subparsers = parser.add_subparsers(required=True, dest="subcommand")

    parser_install = subparsers.add_parser("install")
    parser_launcher = subparsers.add_parser("launch")
    parser_webext_native_client = subparsers.add_parser("webext-native-client")

    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)

    args = parser.parse_args()
    if args.subcommand == "install":
        subcommands.install()
    if args.subcommand == "launch":
        subcommands.launch()
    elif args.subcommand == "webext-native-client":
        subcommands.webext_native_client()
    else:
        print("Subcommand not found")
        exit(1)
