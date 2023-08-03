def plain(diff, parent=''):

    def inner(diff, parent=''):
        result = ''

        for item in diff:

            if 'children' in item:
                result += inner(item['children'])

            elif item['file_1'] is None:
                result += 'Property ' + "'" + item['path'] + item['key'] + "'"
                result += ' was added with value: '
                result += format_val(item['file_2']) + '\n'

            elif item['file_2'] is None:
                result += 'Property ' + "'" + item['path'] + item['key'] + "'"
                result += ' was removed\n'

            elif item['file_1'] != item['file_2'] \
                    and item['file_1'] is not None \
                    and item['file_2'] is not None:
                result += 'Property ' + "'" + item['path'] + item['key'] + "'"
                result += ' was updated. From '
                result += format_val(item['file_1'])
                result += ' to '
                result += format_val(item['file_2'])
                result += '\n'

        return result

    return inner(diff)


def format_val(val):
    if isinstance(val, dict):
        return '[complex value]'
    if val == 'false':
        return 'false'
    if val == 'true':
        return 'true'
    if val == 'null':
        return 'null'
    if isinstance(val, str):
        return "'" + val + "'"
    else:
        return str(val)
