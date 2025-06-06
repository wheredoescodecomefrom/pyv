import argparse
from version_manager import set_version, get_current_version, list_versions, uninstall_version
from installer import install_version
from registry import fetch_available_versions
from doctor import doctor
from utils import exec_command, clean

def main():
    parser = argparse.ArgumentParser(prog="pyv", description="Python version manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # pyv install <version>
    install_parser = subparsers.add_parser("install", help="Install a specific Python version")
    install_parser.add_argument("version", help="Python version to install (e.g. 3.12.2)")

    # pyv use <version>
    use_parser = subparsers.add_parser("use", help="Set the global Python version")
    use_parser.add_argument("version", help="Python version to use globally")

    # pyv uninstall <version>
    uninstall_parser = subparsers.add_parser("uninstall", help="Uninstall a specific Python version")
    uninstall_parser.add_argument("version", help="Python version to uninstall")

    # pyv available
    available_parser = subparsers.add_parser("available", help="List available Python versions")

    # pyv current
    subparsers.add_parser("current", help="Show the current Python version")

    # pyv list
    subparsers.add_parser("list", help="List all installed Python versions")

    # pyv doctor
    subparsers.add_parser("doctor", help="Check for issues with the installation")

    # pyv exec
    exec_parser = subparsers.add_parser("exec", help="Run a command with a specific python version")
    exec_parser.add_argument("version")
    exec_parser.add_argument("command", nargs=argparse.REMAINDER)

    # pyv clean
    clean_parser = subparsers.add_parser("clean", help="Clean up the installation")

    args = parser.parse_args()

    if args.command == "install":
        install_version(args.version)
    elif args.command == "use":
        set_version(args.version)
    elif args.command == "uninstall":
        uninstall_version(args.version)
    elif args.command == "available":
        for v in fetch_available_versions():
            print(v)
    elif args.command == "current":
        print(get_current_version())
    elif args.command == "list":
        for v in list_versions():
            print(f"- {v}")
    elif args.command == "doctor":
        doctor()
    elif args.command == "clean":
        clean()
    elif args.command == "exec":
        exec_command(args.version, args.command)

if __name__ == "__main__":
    main()
