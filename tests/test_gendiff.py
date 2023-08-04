import pytest

from gendiff.get_diff import generate_diff


@pytest.fixture
def plain1():
    return '/Users/Number1/PycharmProjects/python-project-50/tests/fixtures/plain1.json'


@pytest.fixture
def plain2():
    return '/Users/Number1/PycharmProjects/python-project-50/tests/fixtures/plain2.json'


def test_stylish_formatter_plain_files(plain1, plain2):
    assert generate_diff(plain1, plain2) == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'


def test_plain_formatter_plain_files(plain1, plain2):
    assert generate_diff(plain1, plain2, formatter='plain') == "Property 'follow' was removed\nProperty 'proxy' was removed\nProperty 'timeout' was updated. From 50 to 20\nProperty 'verbose' was added with value: true"
