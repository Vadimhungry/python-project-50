def plain(diff):
    return plainize(diff)[:-1]


def plainize(diff):

    def inner(diff, path=''):
        result = ''
        for item in diff:
            match item['action']:

                case 'nested':
                    result += inner(
                        item['children'],
                        path + str(item['key']) + '.'
                    )

                case 'added':
                    result += 'Property ' + "'"
                    result += path + item['key'] + "'"
                    result += ' was added with value: '
                    result += format_val(item['new_value']) + '\n'

                case 'deleted':
                    result += 'Property ' + "'"
                    result += path + item['key'] + "'"
                    result += ' was removed\n'

                case 'updated':
                    result += 'Property ' + "'"
                    result += path + item['key'] + "'"
                    result += ' was updated. From '
                    result += format_val(item['old_value'])
                    result += ' to '
                    result += format_val(item['new_value']) + '\n'

        return result
    return inner(diff)


def format_val(val):
    if isinstance(val, dict):
        return '[complex value]'
    if val is False:
        return 'false'
    if val is True:
        return 'true'
    if val is None:
        return 'null'
    if isinstance(val, str):
        return "'" + val + "'"
    else:
        return str(val)
