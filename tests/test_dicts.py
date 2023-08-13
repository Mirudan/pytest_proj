import pytest
from utils import dicts


@pytest.fixture
def list_fixture():
    return {'a': 1, 'b': 2, 'c': 3}

def test_val(list_fixture):
    assert dicts.get_val(list_fixture, 'd', '=(') == '=('
    assert dicts.get_val(list_fixture, 'c') == 3
    assert dicts.get_val({}, 'c') == 'git'
