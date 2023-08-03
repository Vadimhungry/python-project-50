def plain(diff, parent=''):

    def inner(diff, parent=''):
        result = ''

        for item in diff:

            if 'children' in item:
                result += inner(item['children'])

            elif item['file_1'] is None:
                result += 'Property ' + "'" + item['path'] + item['key'] + "'"
                result += ' was added with value: '
                if isinstance(item['file_2'], dict):
                    result += '[complex value]\n'
                else:
                    result += "'" + str(item['file_2']) + "'" + '\n'

            elif item['file_2'] is None:
                result += 'Property ' + "'" + item['path'] + item['key'] + "'"
                result += ' was removed\n'

            elif item['file_1'] != item['file_2'] \
                    and item['file_1'] is not None \
                    and item['file_2'] is not None:
                result += 'Property ' + "'" + item['path'] + item['key'] + "'"
                result += ' was updated. From '
                if isinstance(item['file_1'], dict):
                    result += '[complex value]'
                else:
                    result += str(item['file_1'])
                result += ' to '
                if isinstance(item['file_2'], dict):
                    result += '[complex value]'
                else:
                    result += "'" + str(item['file_2']) + "'"
                result += '\n'

        return result

    return inner(diff)
