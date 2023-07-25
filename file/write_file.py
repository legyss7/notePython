import json

def write_file(filename, my_dicts):
    with open(filename, 'w') as f:
        json.dump(my_dicts, f)