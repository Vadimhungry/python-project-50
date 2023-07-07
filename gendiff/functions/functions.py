def make_diff_dict(data1, data2):

    def inner(data1, data2):

        diff = []

        for key in list({**data1, **data2}.keys()):
            if key not in data2:
                print('key not in data2')
                diff.append({
                    'key': key,
                    'file_1': data1[key],
                    'file_2': None,
                    'children': []
                })

            elif key not in data1:
                diff.append({
                    'key': key,
                    'file_1': None,
                    'file_2': data2[key],
                    'children': []
                })

            elif key in data1 and key in data2:

                if isinstance(data1[key], dict) \
                        and isinstance(data2[key], dict):
                    diff.append({
                        'key': key,
                        'children': inner(data1[key], data2[key])
                    })

                elif data1[key] != data2[key]:
                    diff.append({
                        'key': key,
                        'file_1': data1[key],
                        'file_2': data2[key],
                        'children': []
                    })

                elif data1[key] == data2[key]:
                    diff.append({
                        'key': key,
                        'file_1': data1[key],
                        'file_2': data2[key],
                        'children': []
                    })
        return diff

    return inner(data1, data2)


def form_diff_string(diff_dict):
    result = '{'
    for i in sorted(diff_dict.items()):
        result += '\n' + i[1]
    result += '\n}'
    return result


def stringify_dic(obj, replacer=' ', spaces=1):
    baseSpaces = spaces

    def inner(obj, replacer=' ', spaces=1):

        result = ''
        for key, val in obj.items():

            if type(val) == dict:
                result += f'{replacer * spaces}{key}:' + \
                           ' {\n'
                result += f'{inner(val, replacer, spaces + baseSpaces)}' + \
                          f'{replacer * spaces}' + '}\n'
            else:
                result += f'{replacer * spaces}{key}: {val}\n'
        return result
    inner_str = inner(obj, replacer, spaces)
    result = '{\n' + inner_str + '}'
    return result


def stringify(obj, replacer=' ', spaces=1):

    if type(obj) == dict:
        return stringify(obj, replacer, spaces)
    else:
        return str(obj)
