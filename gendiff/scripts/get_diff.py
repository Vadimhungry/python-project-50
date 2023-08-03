from gendiff.scripts.parse_data import get_file_data
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import jsonify


def generate_diff(file1, file2, formatter):

    data1 = get_file_data(file1)
    data2 = get_file_data(file2)

    def inner(data1, data2, level=1, path=''):

        diff = []

        for key in sorted(list({**data1, **data2}.keys())):
            if key not in data2:
                diff.append({
                    'key': key,
                    'file_1': data1[key],
                    'file_2': None,
                    'level': level,
                    'path': path

                })

            elif key not in data1:
                diff.append({
                    'key': key,
                    'file_1': None,
                    'file_2': data2[key],
                    'level': level,
                    'path': path
                })

            elif key in data1 and key in data2:

                if isinstance(data1[key], dict) \
                        and isinstance(data2[key], dict):
                    print(path + str(key) + '.')
                    diff.append({
                        'key': key,

                        'children': inner(
                            data1[key],
                            data2[key],
                            level + 1,
                            path + str(key) + '.'),
                        'level': level,
                    })

                elif data1[key] != data2[key]:
                    diff.append({
                        'key': key,
                        'file_1': data1[key],
                        'file_2': data2[key],
                        'level': level,
                        'path': path
                    })

                elif data1[key] == data2[key]:
                    diff.append({
                        'key': key,
                        'file_1': data1[key],
                        'file_2': data2[key],
                        'level': level,
                        'path': path
                    })
        return diff
    diff = inner(data1, data2)

    match formatter:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'json':
            return jsonify(diff)
