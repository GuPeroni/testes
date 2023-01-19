import json
from uuid import uuid4
from app import jsonify
import os

def record_data(name_folder, name_file, file):
    path = os.getcwd() + "/fake_db/" + name_folder + '/' + name_file
    with open(f'{path}.json', 'w') as record:
        json.dump(file, record)

        return jsonify({"id": f"1 | 07c57da7-5ffd-40d2-a4fb-096af509500b"})