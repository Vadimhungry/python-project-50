def stylish(diff, replacer=' ', spacesCount=1):
    return '{' + stylize(diff, replacer, spacesCount) + '\n}'


def stylize(diff, replacer=' ', spacesCount=1, level=1):

    result = ''

    for item in diff:

        prekey_replacer = replacer * (spacesCount * level * 4 - 2)
        prebracket_replacer = replacer * (spacesCount * level * 4)

        result += '\n'

        match item['action']:

            case 'nested':
                result += prekey_replacer + '  '
                result += item['key'] + ': {'
                result += stylize(
                    item['children'],
                    replacer,
                    spacesCount,
                    level + 1
                )
                result += '\n' + prebracket_replacer + '}'

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

                result += '\n'

                result += prekey_replacer + '+ ' + item['key'] + ': '
                result += to_str(
                    item['new_value'],
                    replacer,
                    spacesCount,
                    level
                )
                # result += '\n' + prebracket_replacer + 'AAA'

    return result


def to_str(argument, replacer=' ', spacesCount=1, level=0):
    result = ''

    if isinstance(argument, dict):
        prekey_replacer = replacer * (spacesCount * level * 4 + 4)
        prebracket_replacer = replacer * (spacesCount * level * 4)

        result += '{'
        for key in argument:

            result += '\n' + prekey_replacer + key + ': '

            result += to_str(
                argument[key],
                replacer,
                spacesCount + 1,
                level
            )
        result += '\n' + prebracket_replacer + '}'

    if isinstance(argument, bool):
        result += str(argument).lower()
    if argument is None:
        result += 'null'
    if isinstance(argument, str):
        result += argument
    if isinstance(argument, int) and not isinstance(argument, bool):
        result += str(argument)

    # else:
    #     match argument:
    #         case True:
    #             result += 'true'
    #         case False:
    #             result += 'false'
    #         case None:
    #             result += 'null'
    #         case _:
    #             result += str(argument)
    #     # result += '\n'

    return result
