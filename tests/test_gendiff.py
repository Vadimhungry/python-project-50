import pytest
from os.path import dirname, abspath
from gendiff.get_diff import generate_diff

TESTS_DIR = dirname(abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


@pytest.fixture
def plain1():
    return f'{FIXTURES_PATH}/plain1.json'


@pytest.fixture
def plain2():
    return f'{FIXTURES_PATH}/plain2.json'


@pytest.fixture
def nested1():
    return f'{FIXTURES_PATH}/file1.json'


@pytest.fixture
def nested2():
    return f'{FIXTURES_PATH}/file2.json'


@pytest.fixture
def stylish_plainfile_result():
    file = open(f'{FIXTURES_PATH}/stylish_plainfile_result.txt', 'r')
    return file.read()


@pytest.fixture
def plain_plainfile_result():
    file = open(f'{FIXTURES_PATH}/plain_plainfile_result.txt')
    return file.read()


@pytest.fixture
def stylish_nestedfile_result():
    file = open(f'{FIXTURES_PATH}/stylish_nested_result.txt')
    return file.read()


def test_plain_files(plain1, plain2, stylish_plainfile_result, plain_plainfile_result):
    assert generate_diff(plain1, plain2) == stylish_plainfile_result
    assert generate_diff(plain1, plain2, formatter='plain') == plain_plainfile_result


def test_nested_files(nested1, nested2, stylish_nestedfile_result):
    assert generate_diff(nested1, nested2) == stylish_nestedfile_result
