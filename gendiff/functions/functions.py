def make_plaindiff(data_1, data_2):
    differences = {}

    def inner(data_1, data_2):
        for key in data_1:

            if key in data_2 and data_1[key] == data_2[key]:
                differences[key] = f'  {key}: {data_1[key]}'

            if key in data_2 and data_1[key] != data_2[key]:
                differences[key] = f'- {key}: {data_1[key]}\n' \
                                         f'+ {key}: {data_2[key]}'

            if key not in data_2:
                differences[key] = f'- {key}: {data_1[key]}'

        for key in data_2:
            if key not in data_1:
                differences[key] = f'+ {key}: {data_2[key]}'
        return differences
    return form_diff_string(inner(data_1, data_2))


def form_diff_string(diff_dict):
    result = '{'
    for i in sorted(diff_dict.items()):
        result += '\n' + i[1]
    result += '\n}'
    return result


data1 = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False,
}
data2 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}

print(repr(make_plaindiff(data1, data2)))
