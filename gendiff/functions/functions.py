def get_diff(data1, data2):

    def inner(data1, data2, level=1):

        diff = []

        for key in sorted(list({**data1, **data2}.keys())):
            if key not in data2:
                diff.append({
                    'key': key,
                    'file_1': data1[key],
                    'file_2': None,
                    'level': level

                })

            elif key not in data1:
                diff.append({
                    'key': key,
                    'file_1': None,
                    'file_2': data2[key],
                    'level': level
                })

            elif key in data1 and key in data2:

                if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                    diff.append({
                        'key': key,
                        'children': inner(data1[key], data2[key], level + 1),
                        'level': level
                    })

                elif data1[key] != data2[key]:
                    diff.append({
                        'key': key,
                        'file_1': data1[key],
                        'file_2': data2[key],
                        'level': level
                    })

                elif data1[key] == data2[key]:
                    diff.append({
                        'key': key,
                        'file_1': data1[key],
                        'file_2': data2[key],
                        'level': level
                    })
        return diff

    return inner(data1, data2)


def stylish(obj, replacer=' ', spacesCount=1):
    baseSpacesCount = spacesCount

    def inner(obj, replacer=' ', spacesCount=1):

        result = ''
        for item in obj:

            if 'children' in item:

                result += replacer * (spacesCount * item['level'] * 4 - 2) + '  ' + item['key'] + ':' + ' {\n'

                result += inner(
                    item['children'],
                    replacer,
                    spacesCount
                ) + replacer * (spacesCount * item['level'] * 4) + '}\n'
            else:

                if item['file_1'] is None:

                    result += replacer * (spacesCount * item['level'] * 4 - 2) + \
                              '+ ' + item['key'] +\
                              ': ' + \
                              format_val(
                                  item['file_2'],
                                  replacer,
                                  spacesCount * item['level'] * 4 - 2,
                                  item['level']
                              ) + '\n'

                if item['file_2'] is None:

                    result += replacer * (spacesCount * item['level'] * 4 - 2) + \
                              '- ' + \
                              item['key'] + \
                              ': ' + \
                              format_val(
                                  item['file_1'],
                                  replacer,
                                  spacesCount + baseSpacesCount
                              ) + '\n'

                if item['file_1'] == item['file_2']:

                    result += replacer * (spacesCount * item['level'] * 4 - 2) + \
                              '  ' + \
                              item['key'] + \
                              ': ' + \
                              format_val(
                                  item['file_1'],
                                  replacer,
                                  spacesCount * item['level'] * 4 - 2
                              ) + '\n'

                if item['file_1'] != item['file_2'] \
                        and item['file_1'] is not None \
                        and item['file_2'] is not None:

                    result += replacer * (spacesCount * item['level'] * 4 - 2) + \
                              '- ' + \
                              item['key'] + \
                              ': ' + \
                              format_val(
                                  item['file_1'],
                                  replacer,
                                  spacesCount + baseSpacesCount,
                                  item['level']
                              ) + '\n' + \
                              replacer * (spacesCount * item['level'] * 4 - 2) + \
                              '+ ' + \
                              item['key'] + \
                              ': ' + \
                              format_val(
                                  item['file_2'],
                                  replacer,
                                  spacesCount * item['level'] * 4,
                                  item['level']
                              ) + \
                              '\n'

        return result
    inner_str = inner(obj, replacer, spacesCount)
    result = '{\n' + inner_str + '}'
    return result


def stringify(obj, replacer=' ', spacesCount=1):

    if type(obj) == dict:
        return stylish(obj, replacer, spacesCount)
    else:
        return str(obj)


def format_dic_val(subdict, replacer=' ', spacesCount=1, level=1):
    baseSpacesCount = spacesCount

    def inner(value, replacer, spacesCount, level):

        result = ''

        for i in value:

            if isinstance(value[i], dict):

                result += replacer * (spacesCount * level * 4 - 2) + \
                          '  ' + \
                          str(i) + \
                          ': {\n'
                result += inner(value[i],
                                replacer,
                                spacesCount + baseSpacesCount,
                                level
                                )
                pass
            else:

                result += replacer * (spacesCount * level + 4)
                result += str(i) + ': ' + str(value[i]) + '\n'
                result += replacer * (spacesCount * level - 4)

        return result
    formatted = '{\n' + inner(subdict, replacer, spacesCount, level) + '}'
    return formatted


def format_val(val, replacer, spacesCount, level=1):

    if isinstance(val, dict):
        return format_dic_val(val, replacer, spacesCount, level)
    else:
        return str(val)
