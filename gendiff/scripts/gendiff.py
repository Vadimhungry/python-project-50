#!/usr/bin/env python3
import argparse
from gendiff.formatters.plain import plain
from gendiff.scripts.get_diff import generate_diff
from gendiff.formatters.stylish import stylish
from gendiff.scripts.parse_data import get_file_data
from gendiff.formatters.json import jsonify


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
parser.add_argument('first_file', type=str, help='First file')
parser.add_argument('second_file', type=str, help='Second_file')
parser.add_argument(
    '-f',
    '--format',
    type=str,
    default='stylish',
    help='set format of output'
)
args = parser.parse_args()


def main():
    data_1 = get_file_data(args.first_file)
    data_2 = get_file_data(args.second_file)
    formatter = args.format
    diff = generate_diff(data_1, data_2)
    match formatter:
        case 'stylish':
            print(stylish(diff))
        case 'plain':
            print(plain(diff))
        case 'json':
            print(jsonify(diff))


if __name__ == '__main__':
    main()
