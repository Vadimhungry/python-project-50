from gendiff.parse_data import get_file_data
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import jsonify


def generate_diff(file1, file2, formatter='stylish'):

    data1 = get_file_data(file1)
    data2 = get_file_data(file2)

    def inner(data1, data2, level=1, path=''):

        diff = []

        for key in sorted(list({**data1, **data2}.keys())):

            if key not in data2:
                diff.append({
                    'key': key,
                    'action': 'deleted',
                    'file_1': data1[key],
                    # 'file_2': None,
                    'level': level,
                    'path': path

                })

            elif key not in data1:
                diff.append({
                    'key': key,
                    'action': 'added',
                    # 'file_1': None,
                    'file_2': data2[key],
                    'level': level,
                    'path': path
                })

            elif key in data1 and key in data2:

                if isinstance(data1[key], dict) \
                        and isinstance(data2[key], dict):
                    diff.append({
                        'key': key,
                        'action': 'nested',
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
                        'action': 'updated',
                        'file_1': data1[key],
                        'file_2': data2[key],
                        'level': level,
                        'path': path
                    })

                elif data1[key] == data2[key]:
                    diff.append({
                        'key': key,
                        'action': 'unchanged',
                        'file_1': data1[key],
                        'file_2': data2[key],
                        'level': level,
                        'path': path
                    })
        return diff

    diff = inner(data1, data2)
    # print(diff)
    return format_diff(diff, formatter)


# def parse_val(val):
#     if isinstance(val, bool):
#         return str(val).lower()
#     if val is None:
#         return 'null'
#     else:
#         return val


def format_diff(diff, formatter):
    match formatter:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'json':
            return jsonify(diff)


[
    {
        'key': 'common',
        'action': 'nested',
        'children':
            [
                {
                    'key': 'follow',
                    'action': 'added',
                    'file_2': False,
                    'level': 2,
                    'path': 'common.'
                },
                {
                    'key': 'setting1',
                    'action': 'unchanged',
                    'file_1': 'Value 1',
                    'file_2': 'Value 1',
                    'level': 2,
                    'path': 'common.'
                },
                {
                    'key': 'setting2',
                    'action': 'deleted',
                    'file_1': 200,
                    'level': 2,
                    'path': 'common.'
                },
                {
                    'key': 'setting3',
                    'action': 'updated',
                    'file_1': True,
                    'file_2': {'key': 'value'},
                    'level': 2,
                    'path': 'common.'
                },
                {
                    'key': 'setting4',
                    'action': 'added',
                    'file_2': 'blah blah',
                    'level': 2,
                    'path': 'common.'
                },
                {
                    'key': 'setting5',
                    'action': 'added',
                    'file_2': {'key5': 'value5'},
                    'level': 2,
                    'path': 'common.'
                },
                {
                    'key': 'setting6',
                    'action': 'nested',
                    'children':
                        [
                            {
                                'key': 'doge',
                                'action': 'nested',
                                'children':
                                    [
                                        {
                                            'key': 'wow',
                                            'action': 'updated',
                                            'file_1': 'too much',
                                            'file_2': 'so much',
                                            'level': 4,
                                            'path': 'common.setting6.doge.'
                                        }
                                    ],
                                'level': 3
                            },
                            {
                                'key': 'key',
                                'action': 'unchanged',
                                'file_1': 'value',
                                'file_2': 'value',
                                'level': 3,
                                'path': 'common.setting6.'
                            },
                            {'key': 'ops', 'action': 'added', 'file_2': 'vops', 'level': 3, 'path': 'common.setting6.'}
                        ],
                    'level': 2
                }
            ],
        'level': 1
    },
    {
        'key': 'group1',
        'action': 'nested',
        'children':
            [
                {
                    'key': 'baz',
                    'action': 'updated',
                    'file_1': 'bas',
                    'file_2': 'bars',
                    'level': 2,
                    'path': 'group1.'
                },
                {
                    'key': 'foo',
                    'action': 'unchanged',
                    'file_1': 'bar',
                    'file_2': 'bar',
                    'level': 2,
                    'path': 'group1.'
                },
                {
                    'key': 'nest',
                    'action': 'updated',
                    'file_1': {'key': 'value'},
                    'file_2': 'str',
                    'level': 2,
                    'path': 'group1.'
                }
            ],
        'level': 1},
    {
        'key': 'group2',
        'action': 'deleted',
        'file_1': {'abc': 12345, 'deep': {'id': 45}},
        'level': 1,
        'path': ''
    },
    {
        'key': 'group3',
        'action': 'added',
        'file_2': {'deep': {'id': {'number': 45}}, 'fee': 100500},
        'level': 1, 'path': ''},
    {
        'key': 'group4',
        'action': 'nested',
        'children':
            [
                {
                    'key': 'default',
                    'action': 'updated',
                    'file_1': None,
                    'file_2': '',
                    'level': 2, 'path': 'group4.'}, {'key': 'foo', 'action': 'updated', 'file_1': 0, 'file_2': None, 'level': 2, 'path': 'group4.'}, {'key': 'isNested', 'action': 'updated', 'file_1': False, 'file_2': 'none', 'level': 2, 'path': 'group4.'}, {'key': 'key', 'action': 'added', 'file_2': False, 'level': 2, 'path': 'group4.'}, {'key': 'nest', 'action': 'nested', 'children': [{'key': 'bar', 'action': 'updated', 'file_1': '', 'file_2': 0, 'level': 3, 'path': 'group4.nest.'}, {'key': 'isNested', 'action': 'deleted', 'file_1': True, 'level': 3, 'path': 'group4.nest.'}], 'level': 2}, {'key': 'someKey', 'action': 'added', 'file_2': True, 'level': 2, 'path': 'group4.'}, {'key': 'type', 'action': 'updated', 'file_1': 'bas', 'file_2': 'bar', 'level': 2, 'path': 'group4.'}], 'level': 1}]
