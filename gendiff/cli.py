import argparse


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference. '
                    'Supported file extensions: json, yml(yaml)'
    )
    parser.add_argument('first_file', type=str, help='Path to first file.')
    parser.add_argument('second_file', type=str, help='Path to second file.')
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='stylish',
        help='set format of output. '
             'Available formats: stylish(default), plain, json'
    )
    args = parser.parse_args()

    return args.first_file, args.second_file, args.format
