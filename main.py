import os
import json

def load_ignore_list(json_path):
    """
    Loads ignore list from a JSON file.
    
    Args:
        json_path (str): Path to the JSON file
        
    Returns:
        list: List of items to ignore
    """
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
            # Assuming the JSON contains either a list or a dict with an "ignore" key
            return data if isinstance(data, list) else data.get("ignore_names", [])
    except FileNotFoundError:
        print(f"Warning: Ignore file {json_path} not found. Using empty ignore list.")
        return []
    except json.JSONDecodeError:
        print(f"Warning: Invalid JSON in {json_path}. Using empty ignore list.")
        return []

def print_directory_tree(dir_path, ignore_list=None, indent="", prefix=""):
    """
    Prints a directory tree structure, ignoring items in the ignore_list.
    
    Args:
        dir_path (str): Path to the directory
        ignore_list (list): List of names to ignore (files/directories)
        indent (str): Indentation string for current level
        prefix (str): Prefix for the current item
    """
    if ignore_list is None:
        ignore_list = []
    
    try:
        items = os.listdir(dir_path)
    except PermissionError:
        print(f"{indent}{prefix}Permission denied: {dir_path}")
        return
    
    items.sort()
    items = [item for item in items if item not in ignore_list]
    
    for index, item in enumerate(items):
        path = os.path.join(dir_path, item)
        is_last = index == len(items) - 1
        current_prefix = "└── " if is_last else "├── "
        
        print(f"{indent}{current_prefix}{item}")
        
        if os.path.isdir(path):
            new_indent = indent + ("    " if is_last else "│   ")
            print_directory_tree(path, ignore_list, new_indent, "")

# Example usage
if __name__ == "__main__":
    # Path to your directory and JSON file
    directory = "."  # Current directory
    ignore_json_path = "ignore.json"
    
    # Load ignore list from JSON
    ignore_list = load_ignore_list(ignore_json_path)
    
    print(f"Directory tree for: {os.path.abspath(directory)}")
    print_directory_tree(directory, ignore_list)