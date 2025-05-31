import argparse
import sys

def main() -> None:
    parser = argparse.ArgumentParser(
        description="mdv: Markdown viewer, in the terminal."
    )
    parser.add_argument(
        "filename",
        nargs="?",
        help="Markdown file to view"
    )
    args = parser.parse_args()

    if not args.filename:
        print("Please provide a markdown file to view.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(args.filename, "r") as f:
            content = f.read()
        print(content)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
