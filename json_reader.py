import json

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def write_json_file(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)
