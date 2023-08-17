import pytest
from os.path import dirname, abspath
from gendiff.get_diff import generate_diff

TESTS_DIR = dirname(abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


@pytest.mark.parametrize("file1, file2, output",
                         [
                             ('plain1.json', 'plain2.json', 'stylish_plainfile_result.txt'),
                             ('file1.json', 'file2.json', 'stylish_nested_result.txt')
                         ]
                         )
def test_generate_diff_stylish(file1, file2, output):
    file_1 = f'{FIXTURES_PATH}/{file1}'
    file_2 = f'{FIXTURES_PATH}/{file2}'
    result = (open(f'{FIXTURES_PATH}/{output}', 'r')).read()
    assert generate_diff(file_1, file_2) == result


@pytest.mark.parametrize("file1, file2, output",
                         [
                             ('plain1.json', 'plain2.json', 'plain_plainfile_result.txt'),
                             ('file1.json', 'file2.json', 'plain_nestedfile_result.txt')
                         ]
                         )
def test_generate_diff_plain(file1, file2, output):
    file_1 = f'{FIXTURES_PATH}/{file1}'
    file_2 = f'{FIXTURES_PATH}/{file2}'
    result = (open(f'{FIXTURES_PATH}/{output}', 'r')).read()
    assert generate_diff(file_1, file_2, formatter='plain') == result
