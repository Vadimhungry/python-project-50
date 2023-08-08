def stylish(diff, replacer=' ', spacesCount=1):

    def inner(diff, replacer=' ', spacesCount=1):

        result = ''

        for item in diff:

            prekey_replacer = replacer * (spacesCount * item['level'] * 4 - 2)
            prebracket_replacer = replacer * (spacesCount * item['level'] * 4)

            match item['action']:

                case 'nested':
                    result += prekey_replacer + '  '
                    result += item['key'] + ':' + ' {\n'
                    result += inner(
                        item['children'],
                        replacer,
                        spacesCount
                    )
                    result += prebracket_replacer + '}\n'

                case 'added':
                    result += prekey_replacer + '+ ' + item['key'] + ': '
                    if isinstance(item['file_2'], dict):

                        result += format_dict_val(
                            item['file_2'],
                            replacer,
                            spacesCount,
                            item['level']
                        )
                        result += '\n'
                    else:
                        result += format_plain_val(item['file_2']) + '\n'

                case 'deleted':
                    result += prekey_replacer + '- ' + item['key'] + ': '
                    if isinstance(item['file_1'], dict):

                        result += format_dict_val(
                            item['file_1'],
                            replacer,
                            spacesCount,
                            item['level']
                        )
                        result += '\n'
                    else:
                        result += format_plain_val(item['file_1']) + '\n'

                case 'unchanged':
                    result += prekey_replacer + '  ' + item['key'] + ': '
                    if isinstance(item['file_1'], dict):

                        result += format_dict_val(
                            item['file_1'],
                            replacer,
                            spacesCount,
                            item['level']
                        )
                        result += '\n'
                    else:
                        result += format_plain_val(item['file_1']) + '\n'

                case 'updated':
                    result += prekey_replacer + '- ' + item['key'] + ': '
                    if isinstance(item['file_1'], dict):

                        result += format_dict_val(
                            item['file_1'],
                            replacer,
                            spacesCount,
                            item['level']
                        )
                        result += '\n'
                    else:
                        result += format_plain_val(item['file_1']) + '\n'

                    result += prekey_replacer + '+ ' + item['key'] + ': '

                    if isinstance(item['file_2'], dict):

                        result += format_dict_val(
                            item['file_2'],
                            replacer,
                            spacesCount,
                            item['level']
                        )
                        result += '\n'
                    else:
                        result += format_plain_val(item['file_2']) + '\n'

        return result
    result = '{\n' + inner(diff, replacer, spacesCount) + '}'
    return result


def format_dict_val(argument, replacer=' ', spacesCount=1, level=0):

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
                result += format_plain_val(argument[key])

        result += '\n' + prebracket_replacer + '}'

        return result

    return inner(argument, replacer, spacesCount, level)


def format_plain_val(val):
    match val:
        case True:
            return 'true'
        case False:
            return 'false'
        case None:
            return 'null'
        case _:
            return str(val)
