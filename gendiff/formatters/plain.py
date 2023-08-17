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
                result.append('Property ' + "'")
                result.append(path + item['key'] + "'")
                result.append(' was added with value: ')
                result.append(format_val(item['new_value']) + '\n') 

            case 'deleted':
                result.append('Property ' + "'")
                result.append(path + item['key'] + "'")
                result.append(' was removed\n')

            case 'updated':
                result.append('Property ' + "'")
                result.append(path + item['key'] + "'")
                result.append(' was updated. From ')
                result.append(format_val(item['old_value']))
                result.append(' to ')
                result.append(format_val(item['new_value']) + '\n')

    return ''.join(result)


def format_val(val):
    if isinstance(val, dict):
        return '[complex value]'
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, str):
        return "'" + val + "'"
    if val is None:
        return 'null'
    else:
        return str(val)
