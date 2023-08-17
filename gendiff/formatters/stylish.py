def stylish(diff, replacer=' ', spacesCount=1):
    return '{' + stylize(diff, replacer, spacesCount) + '\n}'


def stylize(diff, replacer=' ', spacesCount=1, level=1):

    result = []

    for item in diff:

        prekey_replacer = replacer * (spacesCount * level * 4 - 2)
        prebracket_replacer = replacer * (spacesCount * level * 4)

        result.append('\n')

        match item['action']:

            case 'nested':
                result.append(f'{prekey_replacer}  {item["key"]}: {"{"}')
                result.append(
                    stylize(
                        item['children'],
                        replacer,
                        spacesCount,
                        level + 1
                    )
                )
                result.append(f'\n{prebracket_replacer}{"}"}')

            case 'added':
                result.append(f'{prekey_replacer}+ {item["key"]}: ')
                result.append(
                    to_str(
                        item['new_value'],
                        replacer,
                        spacesCount,
                        level
                    )
                )

            case 'deleted':
                result.append(f'{prekey_replacer}- {item["key"]}: ')
                result.append(
                    to_str(
                        item['old_value'],
                        replacer,
                        spacesCount,
                        level
                    )
                )

            case 'unchanged':
                result.append(f'{prekey_replacer}  {item["key"]}: ')
                result.append(
                    to_str(
                        item['old_value'],
                        replacer,
                        spacesCount,
                        level
                    )
                )

            case 'updated':
                result.append(f'{prekey_replacer}- {item["key"]}: ')
                result.append(
                    to_str(
                        item['old_value'],
                        replacer,
                        spacesCount,
                        level
                    )
                )
                result.append('\n')

                result.append(prekey_replacer + '+ ' + item['key'] + ': ')
                result.append(
                    to_str(
                        item['new_value'],
                        replacer,
                        spacesCount,
                        level
                    )
                )

    return ''.join(result)


def to_str(argument, replacer=' ', spacesCount=1, level=0):
    result = []

    if isinstance(argument, dict):
        prekey_replacer = replacer * (spacesCount * level * 4 + 4)
        prebracket_replacer = replacer * (spacesCount * level * 4)

        result.append('{')
        for key in argument:

            result.append(f'\n{prekey_replacer}{key}: ')

            result.append(
                to_str(
                    argument[key],
                    replacer,
                    spacesCount + 1,
                    level
                )
            )
        result.append(f'\n{prebracket_replacer}{"}"}')

    if isinstance(argument, bool):
        result.append(str(argument).lower())
    if argument is None:
        result.append('null')
    if isinstance(argument, str):
        result.append(argument)
    if isinstance(argument, int) and not isinstance(argument, bool):
        result.append(str(argument))

    return ''.join(result)
