import pytest
from utils import dicts


def test_val():
    assert dicts.get_val({'a': 1, 'b': 2, 'c': 3}, 'd', '=(') == '=('
    assert dicts.get_val({'a': 1, 'b': 2, 'c': 3}, 'c') == 3
    assert dicts.get_val({}, 'c') == 'git'
