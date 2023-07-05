def make_diff(data1, data2):
    diff = {}


    def inner(data1, data2):

        for key in {**data1, **data2}:

            if key in data1 and key in data2:

                if data1[key] == data2[key]:
                    diff[key] = f'  {key}: {data1[key]}'

                elif type(data1[key]) != dict or type(data2[key]) != dict:
                    diff[key] = f'- {key}: {data1[key]}\n+ {key}: {data2[key]}'

                elif type(data1[key]) == dict:

                    diff[key] = f'{key}: '
                    diff[key] += str(make_diff(data1[key], data2[key]))

            if key in data1 and key not in data2:
                diff[key] = f'- {key}: {data1[key]}'

            if key not in data1 and key in data2:
                diff[key] = f'+ {key}: {data2[key]}'

        return diff

    return inner(data1, data2)

def form_diff_string(diff_dict):
    result = '{'
    for i in sorted(diff_dict.items()):
        result += '\n' + i[1]
    result += '\n}'
    return result


def stringify_dic(obj, replacer=' ', spacesCount=1):
    baseSpacesCount = spacesCount

    def inner(obj, replacer=' ', spacesCount=1):

        result = ''
        for key, val in obj.items():

            if type(val) == dict:
                result += f'{replacer * spacesCount}{key}:' + \
                           ' {\n'
                result += f'{inner(val, replacer , spacesCount + baseSpacesCount)}' + \
                          f'{replacer * spacesCount}' + '}\n'
            else:
                result += f'{replacer * spacesCount}{key}: {val}\n'
        return result
    inner_str = inner(obj, replacer, spacesCount)
    result = '{\n' + inner_str + '}'
    return result


def stringify(obj, replacer=' ', spacesCount=1):

    if type(obj) == dict:
        return stringify_dic(obj, replacer, spacesCount)
    else:
        return str(obj)



