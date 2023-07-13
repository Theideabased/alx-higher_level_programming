#!/usr/bin/python3
""" add all agruement, save the file in json """


import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
from typing import List
import os.path

file_path = 'add_item.json'
data = []
save_to_json_file(data, file_path)
    
load_from_json_file(file_path)

# Get the command-line arguments
arguments = sys.argv[1:]

# Load existing data from file if it exists, or initialize an empty list
file_path = 'add_item.json'
if os.path.exists(file_path):
    existing_data = load_from_json_file(file_path)
else:
    existing_data = []
existing_data = []
# Append the new arguments to the existing data
updated_data = existing_data + arguments

# Save the updated data to the file
save_to_json_file(updated_data, file_path)
