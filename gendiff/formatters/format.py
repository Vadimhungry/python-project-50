from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import jsonify


def format_diff(diff, formatter):
    match formatter:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'json':
            return jsonify(diff)
        case _:
            raise Exception(
                f'Formatter "{formatter}" does not exist! Use "gendiff -h" to find formats available'
            )
