def plain(diff):
    return plainize(diff)


def plainize(diff, path=''):
    result = []
    for item in diff:
        match item['action']:

            case 'nested':
                result.append(
                    plainize(
                        item['children'],
                        f'{path}{str(item["key"])}.'
                    )
                )

            case 'added':
                result.append(
                    f"Property '{path}{item['key']}' was added with value: "
                    f"{format_val(item['new_value'])}"
                )

            case 'deleted':
                result.append(
                    f"Property '{path}{item['key']}' was removed"
                )

            case 'updated':
                result.append(
                    f"Property '{path}{item['key']}' was updated. "
                    f"From {format_val(item['old_value'])} "
                    f"to {format_val(item['new_value'])}"
                )

    return '\n'.join(result)


def format_val(val):
    if val is None:
        return 'null'
    if isinstance(val, dict):
        return '[complex value]'
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, str):
        return f"'{val}'"
    return str(val)
