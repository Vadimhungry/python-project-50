import pytest

from gendiff.scripts.get_diff import generate_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


@pytest.fixture
def data1():
    return {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}


@pytest.fixture
def data2():
    return {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


def test_make_plaindiff(data1, data2):
    assert stylish(generate_diff(data1, data2)) == '{\n  - follow: False\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}'


def test_plain_formatter(data1, data2):
    assert plain(generate_diff(data1, data2)) == "Property 'follow' was removed\nProperty 'proxy' was removed\nProperty 'timeout' was updated. From 50 to '20'\nProperty 'verbose' was added with value: 'True' \n"
