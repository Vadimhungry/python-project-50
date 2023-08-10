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
def stylish_plainfile_result():
    file = open(f'{FIXTURES_PATH}/stylish_plainfile_result.txt', 'r')
    return file.read()


@pytest.fixture
def plain_plainfile_result():
    file = open('/Users/Number1/PycharmProjects/python-project-50/tests/fixtures/plain_plainfile_result.txt')
    return file.read()


def test_stylish_formatter_plain_files(plain1, plain2, stylish_plainfile_result):
    assert generate_diff(plain1, plain2) == stylish_plainfile_result


def test_plain_formatter_plain_files(plain1, plain2, plain_plainfile_result):
    assert generate_diff(plain1, plain2, formatter='plain') == plain_plainfile_result
