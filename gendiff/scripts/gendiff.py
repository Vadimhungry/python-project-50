#!/usr/bin/env python3
from gendiff.scripts.get_diff import generate_diff
from gendiff.scripts.agrparse_work \
    import create_parser, get_formatter, get_paths_to_file1_and_file2


def main():
    parser = create_parser()
    formatter = get_formatter(parser)
    path_to_file1, path_to_file2 = get_paths_to_file1_and_file2(parser)
    diff_formatted = generate_diff(path_to_file1, path_to_file2, formatter)
    print(diff_formatted)


if __name__ == '__main__':
    main()
