#!/usr/bin/env python3
from gendiff.get_diff import generate_diff
from gendiff.argparse_work import parse


def main():
    path_to_file1, path_to_file2, formatter = parse()
    diff_formatted = generate_diff(path_to_file1, path_to_file2, formatter)
    print(diff_formatted)


if __name__ == '__main__':
    main()
