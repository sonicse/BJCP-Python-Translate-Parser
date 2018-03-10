import json


def dump_json(obj, filename='dump.json'):
    with open(filename, 'w') as f:
        json.dump(obj, f)


def read_json(filename='dump.json'):
    with open(filename, 'r') as f:
        obj = json.load(f)
    return obj
