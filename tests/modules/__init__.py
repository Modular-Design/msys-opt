import pytest
from msys.registration import get_modules


@pytest.mark.parametrize(
    "key, exists",
    [
        ("math", True),
        ("sql", True),
        ("math", True),
        ("dont exist", False),
    ],
)
def test_get_modules(key, exists):
    modules = get_modules()
    assert (key in modules.keys()) == exists