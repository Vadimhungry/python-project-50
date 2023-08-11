from gendiff.parse_data import get_file_data
from gendiff.formatters.format import format_diff


def generate_diff(file1, file2, formatter='stylish'):

    data1 = get_file_data(file1)
    data2 = get_file_data(file2)
    diff = build_diff_tree(data1, data2)
    return format_diff(diff, formatter)


def build_diff_tree(data1, data2):
    diff = []

    for key in sorted(list({**data1, **data2}.keys())):

        if key not in data2:
            diff.append({
                'key': key,
                'action': 'deleted',
                'old_value': data1[key]
            })

        elif key not in data1:
            diff.append({
                'key': key,
                'action': 'added',
                'new_value': data2[key]
            })

        elif key in data1 and key in data2:

            if isinstance(data1[key], dict) \
                    and isinstance(data2[key], dict):
                diff.append({
                    'key': key,
                    'action': 'nested',
                    'children': build_diff_tree(
                        data1[key],
                        data2[key]
                    )
                })

            elif data1[key] != data2[key]:
                diff.append({
                    'key': key,
                    'action': 'updated',
                    'old_value': data1[key],
                    'new_value': data2[key],
                })

            elif data1[key] == data2[key]:
                diff.append({
                    'key': key,
                    'action': 'unchanged',
                    'old_value': data1[key],
                    'new_value': data2[key]
                })
    return diff
