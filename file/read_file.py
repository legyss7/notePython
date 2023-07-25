import json


def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read();
        my_dicts = json.loads(data)
    return my_dicts