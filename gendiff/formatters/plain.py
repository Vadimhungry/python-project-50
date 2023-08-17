def plain(diff):
    return plainize(diff)[:-1]


def plainize(diff, path=''):
    result = []
    for item in diff:
        match item['action']:

            case 'nested':
                result.append(
                    plainize(
                        item['children'],
                        path + str(item['key']) + '.'
                    )
                )

            case 'added':
                result.append(
                    f"Property '{path}{item['key']}' was added with value: "
                )
                result.append(
                    f"{format_val(item['new_value'])}\n"
                )

            case 'deleted':
                result.append(
                    f"Property '{path}{item['key']}' was removed\n"
                )

            case 'updated':
                result.append(
                    f"Property '{path}{item['key']}'"
                )
                result.append(
                    f' was updated. From {format_val(item["old_value"])}'
                )
                result.append(
                    f' to {format_val(item["new_value"])}\n'
                )

    return ''.join(result)


def format_val(val):
    if isinstance(val, dict):
        return '[complex value]'
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, str):
        return f"'{val}'"
    if val is None:
        return 'null'
    else:
        return str(val)
