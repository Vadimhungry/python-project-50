import json
import yaml
from yaml.loader import SafeLoader
import os


def get_file_data(file):
    _, file_extension = os.path.splitext(file)
    content = open(file, 'r')
    return parse(content, file_extension)


def parse(content, format):

    match format:
        case '.json':
            return json.load(content)
        case '.yml' | '.yaml':
            return yaml.load(content, Loader=SafeLoader)
        case _:
            raise Exception(f'Unknown extension: "{format}"! I can\'t parse it!')
