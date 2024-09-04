#! /bin/bash

# Creating the file to save the file path you want to use
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
touch "$SCRIPT_DIR/src/file_path.txt"

# Setting the alias
echo "Place this command in you .zshrc or .bashrc file: "
echo "alias task-cli='$SCRIPT_DIR/task-cli.py'"
echo "Than run 'source .zshrc or .bashrc'"