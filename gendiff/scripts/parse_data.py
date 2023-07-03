import json
import yaml
from yaml.loader import SafeLoader
import os


def get_file_extension(file):
    _, file_extension = os.path.splitext(file)
    return file_extension


def get_file_data(file):
    format = get_file_extension(file)

    match format:
        case '.json':
            return parse_json(file)
        case '.yml' | '.yaml':
            return parse_yaml(file)
        case _:
            print("Unknown extension! I can't parse it!")


def parse_json(file):
    with open(file) as data_file:
        data = json.load(data_file)
    return data


def parse_yaml(file):
    with open(file) as data_file:
        data = yaml.load(data_file, Loader=SafeLoader)
    return data
