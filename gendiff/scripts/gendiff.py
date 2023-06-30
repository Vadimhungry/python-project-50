#!/usr/bin/env python3
import argparse
import json
import gendiff.functions.functions as fu

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
parser.add_argument('first_file', type=str, help='First file')
parser.add_argument('second_file', type=str, help='Second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def main():
    with open(args.first_file) as first:
        data_1 = json.load(first)
    with open(args.second_file) as second:
        data_2 = json.load(second)

    print(fu.make_plaindiff(data_1, data_2))


if __name__ == '__main__':
    main()
