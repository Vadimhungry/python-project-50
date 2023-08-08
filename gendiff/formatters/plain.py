def plain(diff, parent=''):

    def inner(diff, parent=''):
        result = ''

        for item in diff:
            match item['action']:

                case 'nested':
                    result += inner(item['children'])

                case 'added':
                    result += 'Property ' + "'"
                    result += item['path'] + item['key'] + "'"
                    result += ' was added with value: '
                    result += format_val(item['file_2']) + '\n'

                case 'deleted':
                    result += 'Property ' + "'"
                    result += item['path'] + item['key'] + "'"
                    result += ' was removed\n'

                case 'updated':
                    result += 'Property ' + "'"
                    result += item['path'] + item['key'] + "'"
                    result += ' was updated. From '
                    result += format_val(item['file_1'])
                    result += ' to '
                    result += format_val(item['file_2']) + '\n'

        return result

    return inner(diff)[:-1]


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
