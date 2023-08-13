import pytest
from utils import arrs


@pytest.fixture
def dict_fixture():
    return [1, 2, 3]


def test_get(dict_fixture):
    assert arrs.get(dict_fixture, 1, "test") == 2
    assert arrs.get(dict_fixture, -1, 2) == 2
    with pytest.raises(IndexError):
        assert arrs.get([], 0, "test") == "test"


def test_slice(dict_fixture):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(dict_fixture, 1) == [2, 3]
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice(dict_fixture, -1) == [3]
    assert arrs.my_slice(dict_fixture, -4) == [1, 2, 3]
