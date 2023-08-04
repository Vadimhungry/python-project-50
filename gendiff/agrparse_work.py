import argparse


def create_parser():
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
    return parser


def get_formatter(parser):
    return parser.parse_args().format


def get_paths_to_file1_and_file2(parser):
    args = parser.parse_args()
    return args.first_file, args.second_file
