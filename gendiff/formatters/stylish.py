def stylish(diff, replacer=' ', spaces_count=1):
    result = '{\n' + \
             ''.join(flatten(stylize(diff, replacer, spaces_count))) + '}'
    return result


def stylize(diff, replacer=' ', spaces_count=1, level=1):

    result = []

    for item in diff:

        prekey_replacer = replacer * (spaces_count * level * 4 - 2)
        prebracket_replacer = replacer * (spaces_count * level * 4)

        match item['action']:

            case 'nested':
                result.append(
                    prekey_replacer + '  ' + item['key'] + ':' + ' {\n')
                result.append(
                    stylize(
                        item['children'],
                        replacer,
                        spaces_count,
                        level + 1
                    )
                )
                result.append(prebracket_replacer + '}\n')

            case 'added':
                result.append(prekey_replacer + '+ ' + item['key'] + ': ')
                result.append(
                    to_str(
                        item['new_value'],
                        replacer,
                        spaces_count,
                        level
                    )
                )

            case 'deleted':
                result.append(prekey_replacer + '- ' + item['key'] + ': ')
                result.append(
                    to_str(
                        item['old_value'],
                        replacer,
                        spaces_count,
                        level
                    )
                )

            case 'unchanged':
                result.append(prekey_replacer + '  ' + item['key'] + ': ')
                result.append(
                    to_str(
                        item['old_value'],
                        replacer,
                        spaces_count,
                        level
                    )
                )

            case 'updated':
                result.append(prekey_replacer + '- ' + item['key'] + ': ')
                result.append(
                    to_str(
                        item['old_value'],
                        replacer,
                        spaces_count,
                        level
                    )
                )
                result.append(prekey_replacer + '+ ' + item['key'] + ': ')
                result.append(
                    to_str(
                        item['new_value'],
                        replacer,
                        spaces_count,
                        level
                    )

                )

    return result


def to_str(argument, replacer=' ', spaces_count=1, level=0):
    result = ''
    if isinstance(argument, dict):
        prekey_replacer = replacer * (spaces_count * level * 4 + 4)
        prebracket_replacer = replacer * (spaces_count * level * 4)
        result += '{'
        result += '\n' + prekey_replacer + key + ': '
        for key in argument:


            if isinstance(argument[key], dict):
                result += to_str(
                    argument[key],
                    replacer,
                    spaces_count + 1,
                    level
                )
            else:
                match argument:
                    case True:
                        return 'true\n'
                    case False:
                        return 'false\n'
                    case None:
                        return 'null\n'
                    case _:
                        return str(argument) + '\n'

        result += '\n' + prebracket_replacer + ' Й}Й'
        return result + '\n'

    else:
        match argument:
            case True:
                return 'true\n'
            case False:
                return 'false\n'
            case None:
                return 'null\n'
            case _:
                return str(argument) + '\n'


def flatten(tree):
    result = []

    def walk(subtree):
        for item in subtree:

            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)

    walk(tree)

    return result
