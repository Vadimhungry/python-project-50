def stylish(diff, replacer=' ', spacesCount=1):
    result = '{\n' + stylize(diff, replacer, spacesCount) + '}'
    return result


def stylize(diff, replacer=' ', spacesCount=1, level=1):

    result = ''

    for item in diff:

        prekey_replacer = replacer * (spacesCount * level * 4 - 2)
        prebracket_replacer = replacer * (spacesCount * level * 4)

        match item['action']:

            case 'nested':
                result += prekey_replacer + '  '
                result += item['key'] + ':' + ' {\n'
                result += stylize(
                    item['children'],
                    replacer,
                    spacesCount,
                    level + 1
                )
                result += prebracket_replacer + '}\n'

            case 'added':
                result += prekey_replacer + '+ ' + item['key'] + ': '
                result += to_str(
                    item['new_value'],
                    replacer,
                    spacesCount,
                    level
                )

            case 'deleted':
                result += prekey_replacer + '- ' + item['key'] + ': '
                result += to_str(
                    item['old_value'],
                    replacer,
                    spacesCount,
                    level
                )

            case 'unchanged':
                result += prekey_replacer + '  ' + item['key'] + ': '
                result += to_str(
                    item['old_value'],
                    replacer,
                    spacesCount,
                    level
                )

            case 'updated':
                result += prekey_replacer + '- ' + item['key'] + ': '
                result += to_str(
                    item['old_value'],
                    replacer,
                    spacesCount,
                    level
                )

                result += prekey_replacer + '+ ' + item['key'] + ': '
                result += to_str(
                    item['new_value'],
                    replacer,
                    spacesCount,
                    level
                )

    return result


def to_str(val, replacer=' ', spacesCount=1, level=0):

    def format_dict_val(val, replacer=' ', spacesCount=1, level=0):

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

        return inner(val, replacer, spacesCount, level)

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

    if isinstance(val, dict):
        return format_dict_val(val, replacer, spacesCount, level) + '\n'
    else:
        return format_plain_val(val) + '\n'
