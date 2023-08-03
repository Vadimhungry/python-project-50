#!/usr/bin/env python3
import argparse
from gendiff.scripts.get_diff import generate_diff


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
    formatter = args.format
    diff_formatted = generate_diff(args.first_file, args.second_file, formatter)
    print(diff_formatted)


if __name__ == '__main__':
    main()
