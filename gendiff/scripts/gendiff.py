#!/usr/bin/env python3
import argparse
import json

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
parser.add_argument('first_file', type=str, help='First file')
parser.add_argument('second_file', type=str, help='Second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def generate_dic_of_diffs(data_1, data_2):
    differences = {}
    for key in data_1:

        if key in data_2 and data_1[key] == data_2[key]:
            differences[key] = f'  {key}: {data_1[key]}'

        if key in data_2 and data_1[key] != data_2[key]:
            differences[key] = f'- {key}: {data_1[key]}\n' \
                                     f'+ {key}: {data_2[key]}'

        if key not in data_2:
            differences[key] = f'- {key}: {data_1[key]}'

    for key in data_2:
        if key not in data_1:
            differences[key] = f'+ {key}: {data_2[key]}'

    return differences


def print_diff(diff_dict):
    print('{')
    for i in sorted(diff_dict.items()):
        print(i[1])
    print('}')


def main():
    with open(args.first_file) as first:
        data_1 = json.load(first)
    with open(args.second_file) as second:
        data_2 = json.load(second)

    print_diff(generate_dic_of_diffs(data_1, data_2))


if __name__ == '__main__':
    main()
