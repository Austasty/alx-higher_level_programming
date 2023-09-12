#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    
    # Extend the items list with command-line arguments
    items.extend(sys.argv[1:])
    
    # Save the updated items list to the JSON file
    save_to_json_file(items, "add_item.json")
