from app import jsonify
from datetime import datetime
import os
import json

def convert_string_to_datetime(string_datetime):
    return datetime.strptime(string_datetime, '%Y-%m-%d').date()

def return_file_in_path(path_plan):
    return os.listdir(path_plan)[-1] if len(os.listdir(path_plan)) > 0 else None

def read_json(path, file):
    with open(path + file, 'r') as return_json:
        return json.load(return_json)