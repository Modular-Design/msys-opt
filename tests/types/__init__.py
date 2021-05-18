import pytest
from msys.registration import get_types


@pytest.mark.types
@pytest.mark.parametrize(
    "key, exists",
    [
        ("vector", True),
        ("dont exist", False),
    ],
)
def test_find_types(key, exists):
    types = get_types()
    assert (key in types.keys()) == exists