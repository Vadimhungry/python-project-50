def get_diff(data1, data2):

    def inner(data1, data2, level=1):

        diff = []

        for key in sorted(list({**data1, **data2}.keys())):
            if key not in data2:
                diff.append({
                    'key': key,
                    'file_1': data1[key],
                    'file_2': None,
                    'level': level

                })

            elif key not in data1:
                diff.append({
                    'key': key,
                    'file_1': None,
                    'file_2': data2[key],
                    'level': level
                })

            elif key in data1 and key in data2:

                if isinstance(data1[key], dict) \
                        and isinstance(data2[key], dict):
                    diff.append({
                        'key': key,
                        'children': inner(data1[key], data2[key], level + 1),
                        'level': level
                    })

                elif data1[key] != data2[key]:
                    diff.append({
                        'key': key,
                        'file_1': data1[key],
                        'file_2': data2[key],
                        'level': level
                    })

                elif data1[key] == data2[key]:
                    diff.append({
                        'key': key,
                        'file_1': data1[key],
                        'file_2': data2[key],
                        'level': level
                    })
        return diff

    return inner(data1, data2)


def stylish(diff, replacer=' ', spacesCount=1):

    def inner(diff, replacer=' ', spacesCount=1):

        result = ''

        for item in diff:

            prekey_replacer = replacer * (spacesCount * item['level'] * 4 - 2)
            prebracket_replacer = replacer * (spacesCount * item['level'] * 4)

            if 'children' in item:
                result += prekey_replacer + '  ' + item['key'] + ':' + ' {\n'
                result += inner(
                    item['children'],
                    replacer,
                    spacesCount
                )
                result += prebracket_replacer + '}\n'

            else:

                if item['file_1'] is None:

                    result += prekey_replacer + '+ ' + item['key'] + ': '

                    if isinstance(item['file_2'], dict):

                        result += format_value(
                            item['file_2'],
                            replacer,
                            spacesCount,
                            item['level']
                        )
                        result += '\n'
                    else:
                        result += str(item['file_2']) + '\n'

                if item['file_2'] is None:

                    result += prekey_replacer + '- ' + item['key'] + ': '

                    if isinstance(item['file_1'], dict):

                        result += format_value(
                            item['file_1'],
                            replacer,
                            spacesCount,
                            item['level']
                        )
                        result += '\n'
                    else:
                        result += str(item['file_1']) + '\n'

                if item['file_1'] == item['file_2']:
                    result += prekey_replacer + '  ' + item['key'] + ': '

                    if isinstance(item['file_1'], dict):

                        result += format_value(
                            item['file_1'],
                            replacer,
                            spacesCount,
                            item['level']
                        )
                        result += '\n'
                    else:
                        result += str(item['file_1']) + '\n'

                if item['file_1'] != item['file_2'] \
                        and item['file_1'] is not None \
                        and item['file_2'] is not None:

                    result += prekey_replacer + '- ' + item['key'] + ': '

                    if isinstance(item['file_1'], dict):

                        result += format_value(
                            item['file_1'],
                            replacer,
                            spacesCount,
                            item['level']
                        )
                        result += '\n'
                    else:
                        result += str(item['file_1']) + '\n'

                    result += prekey_replacer + '+ ' + item['key'] + ': '

                    if isinstance(item['file_2'], dict):

                        result += format_value(
                            item['file_2'],
                            replacer,
                            spacesCount,
                            item['level']
                        )
                        result += '\n'
                    else:
                        result += str(item['file_2']) + '\n'

        return result
    result = '{\n' + inner(diff, replacer, spacesCount) + '}'
    return result


def format_value(argument, replacer=' ', spacesCount=1, level=0):

    def inner(argument, replacer=' ', spacesCount=1, level=0):
        prekey_replacer = replacer * (spacesCount * level * 4 + 4)
        prebracket_replacer = replacer * (spacesCount * level * 4)
        result = ''

        result += '{'
        for key in argument:

            result += '\n' + prekey_replacer + key + ': '
            if isinstance(argument[key], dict):
                result += inner(
                    argument[key],
                    replacer,
                    spacesCount + 1,
                    level
                )
            else:
                result += str(argument[key])

        result += '\n' + prebracket_replacer + '}'

        return result

    return inner(argument, replacer, spacesCount, level)
