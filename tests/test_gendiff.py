import pytest

from gendiff.functions.functions import get_diff, stylish


@pytest.fixture
def data1():
    return {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}


@pytest.fixture
def data2():
    return {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


def test_make_plaindiff(data1, data2):
    assert stylish(get_diff(data1, data2)) == '{\n  - follow: False\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}'


