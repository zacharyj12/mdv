import argparse
from rich.console import Console
from rich.markdown import Markdown
import sys

def view_markdown_file(filepath):
    console = Console()
    try:
        with open(filepath, "r", encoding="utf-8") as md_file:
            content = md_file.read()
        markdown = Markdown(content)
        console.print(markdown)
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] File not found at '{filepath}'")
    except Exception as e:
        console.print(f"[bold red]An error occurred:[/bold red] {e}")



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
    # The warning suppression is for runtime, this print still works as expected
    print("Please provide a markdown file to view.", file=sys.stderr)
    sys.exit(1)

view_markdown_file(args.filename)