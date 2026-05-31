import argparse
import sys


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    return a + b


def main():
    parser = argparse.ArgumentParser(description="A simple Python CLI tool")
    subparsers = parser.add_subparsers(dest="command")

    # greet command
    greet_parser = subparsers.add_parser("greet", help="Greet someone")
    greet_parser.add_argument("name", help="Name to greet")

    # add command
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float)
    add_parser.add_argument("b", type=float)

    args = parser.parse_args()

    if args.command == "greet":
        print(greet(args.name))
    elif args.command == "add":
        print(add(args.a, args.b))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
