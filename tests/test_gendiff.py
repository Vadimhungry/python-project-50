import pytest
from os.path import dirname, abspath
from gendiff.get_diff import generate_diff


def get_path(file):
    return f"{dirname(abspath(__file__))}/fixtures/{file}"


@pytest.mark.parametrize("file1, file2, output, format",
                         [
                             ('plain1.json', 'plain2.json', 'stylish_plainfile_result.txt', 'stylish'),
                             ('file1.json', 'file2.json', 'stylish_nested_result.txt', 'stylish'),
                             ('plain1.json', 'plain2.json', 'plain_plainfile_result.txt', 'plain'),
                             ('file1.json', 'file2.json', 'plain_nestedfile_result.txt', 'plain'),
                         ]
                         )
def test_generate_diff_stylish(file1, file2, output, format):
    file_1 = get_path(file1)
    file_2 = get_path(file2)
    result = (open(get_path(output), 'r')).read()
    assert generate_diff(file_1, file_2, format) == result
