import json
import yaml
from yaml.loader import SafeLoader
import os


def get_file_data(file):
    _, file_extension = os.path.splitext(file)
    return parse(file, file_extension)


def parse(content, format):
    with open(content) as data_file:
        match format:
            case '.json':
                return json.load(data_file)
            case '.yml' | '.yaml':
                return yaml.load(data_file, Loader=SafeLoader)
            case _:
                print("Unknown extension! I can't parse it!")
