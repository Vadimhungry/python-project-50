def stylish(diff, replacer=' ', spaces_count=1):
    return stylize(diff, replacer, spaces_count)


def stylize(diff, replacer=' ', spaces_count=1, level=1):

    result = []

    for item in diff:

        prekey_replacer = replacer * (spaces_count * level * 4 - 2)
        prebracket_replacer = replacer * (spaces_count * level * 4)

        match item['action']:

            case 'nested':
                result.append(
                    f'{prekey_replacer}  {item["key"]}: {"{"}'
                )
                kids = stylize(
                    item["children"],
                    replacer, spaces_count,
                    level + 1
                )
                result.append(
                    f'{kids}'
                    f'\n{prebracket_replacer}{"}"}'
                )

            case 'added':
                stringed_val = to_str(
                    item["new_value"],
                    replacer,
                    spaces_count,
                    level
                )
                result.append(
                    f'{prekey_replacer}+ {item["key"]}: '
                    f'{stringed_val}'
                )

            case 'deleted':
                stringed_val = to_str(
                    item["old_value"],
                    replacer,
                    spaces_count,
                    level
                )
                result.append(
                    f'{prekey_replacer}- {item["key"]}: '
                    f'{stringed_val}'
                )

            case 'unchanged':
                stringed_val = to_str(
                    item["old_value"],
                    replacer,
                    spaces_count,
                    level
                )
                result.append(
                    f'{prekey_replacer}  {item["key"]}: '
                    f'{stringed_val}'
                )

            case 'updated':
                stringed_old_val = to_str(
                    item["old_value"],
                    replacer,
                    spaces_count,
                    level
                )
                result.append(
                    f'{prekey_replacer}- {item["key"]}: '
                    f'{stringed_old_val}'
                )

                stringed_new_val = to_str(
                    item["new_value"],
                    replacer,
                    spaces_count,
                    level
                )
                result.append(
                    f'{prekey_replacer}+ {item["key"]}: '
                    f'{stringed_new_val}'
                )
    if level == 1:
        result = ['{'] + result + ['}']
    return '\n'.join(result)


def to_str(val, replacer=' ', spaces_count=1, level=0):
    result = []

    if isinstance(val, dict):
        prekey_replacer = replacer * (spaces_count * level * 4 + 4)
        prebracket_replacer = replacer * (spaces_count * level * 4)

        result.append('{')
        for key in val:

            result.append(
                f'\n{prekey_replacer}{key}: '
                f'{to_str(val[key], replacer, spaces_count + 1, level)}'
            )

        result.append(f'\n{prebracket_replacer}{"}"}')

    if isinstance(val, bool):
        result.append(str(val).lower())
    if val is None:
        result.append('null')
    if isinstance(val, str):
        result.append(val)
    if isinstance(val, int) and not isinstance(val, bool):
        result.append(str(val))

    return ''.join(result)
