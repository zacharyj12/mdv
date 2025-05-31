#!/bin/bash

# Check if current directory is 'scripts' and if it is then cd .. because you need to run this from the mdv directory
if [ "$(basename "$PWD")" == "scripts" ]; then
    cd ..
fi


# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Error: uv is not installed. Please install it first."
    exit 1
fi

uv sync
uv pip install -U pyinstaller 
uv run pyinstaller src/mdv.py --name mdv --runtime-hook empty_rthook.py --exclude-module pkg_resources
