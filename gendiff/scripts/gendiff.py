#!/usr/bin/env python3
import argparse
import gendiff.functions.functions as fu
from gendiff.scripts.parse_data import get_file_data

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
parser.add_argument('first_file', type=str, help='First file')
parser.add_argument('second_file', type=str, help='Second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def main():
    data_1 = get_file_data(args.first_file)
    data_2 = get_file_data(args.second_file)

    print(fu.make_diff(data_1, data_2))


if __name__ == '__main__':
    main()
