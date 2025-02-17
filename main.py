import os
import json

def print_directory_tree(root_dir, ignore_list, indent="", is_last=False):
    """
    Prints a directory tree structure, ignoring items in the ignore_list.

    Args:
        root_dir (str): The path to the root directory.
        ignore_list (list): A list of names to ignore (from ignore.json).
        indent (str):  Indentation string for visual hierarchy (internal use).
        is_last (bool): Whether this directory is the last item in its parent (internal use).
    """
    if not os.path.isdir(root_dir):
        print(f"Error: '{root_dir}' is not a valid directory.")
        return

    base_name = os.path.basename(root_dir)

    # Check if current directory name is in ignore list
    if base_name in ignore_list:
        return  # Skip this directory and its contents

    tree_prefix = indent
    if is_last:
        tree_prefix += "└── "
    else:
        tree_prefix += "├── "
    print(tree_prefix + base_name)

    if is_last:
        indent += "    "
    else:
        indent += "│   "

    items = os.listdir(root_dir)
    item_count = len(items)

    for index, item in enumerate(items):
        item_path = os.path.join(root_dir, item)
        is_last_item = (index == item_count - 1)

        # Check if item name is in ignore list BEFORE processing further
        if item in ignore_list:
            continue  # Skip this item

        if os.path.isdir(item_path):
            print_directory_tree(item_path, ignore_list, indent, is_last_item)
        else:
            file_prefix = indent
            if is_last_item:
                file_prefix += "└── "
            else:
                file_prefix += "├── "
            print(file_prefix + item)


if __name__ == "__main__":
    ignore_file = "ignore.json"
    ignore_names = []  # Default to empty list if ignore.json not found or invalid

    try:
        with open(ignore_file, 'r') as f:
            ignore_data = json.load(f)
            ignore_names = ignore_data.get("ignore_names", [])  # Get list, default to empty if key not found
    except FileNotFoundError:
        print(f"Warning: '{ignore_file}' not found. No files/folders will be ignored.")
    except json.JSONDecodeError:
        print(f"Warning: '{ignore_file}' is not a valid JSON file. No files/folders will be ignored.")

    target_directory = ""
    if not target_directory:
        target_directory = "/home/mm/Desktop/42wor.github.io"

    print_directory_tree(target_directory, ignore_names)