import pytest
from msys_opt.core import OptimizableType
from msys.core import Type


@pytest.mark.core
@pytest.mark.connection
@pytest.mark.parametrize(
    "value",
    [
        (None,),
        ([1, 2, 3],),
        (1,),
        ("test",),
    ],
)
def test_create(value):
    t = Type(value)
    assert t.get_value() == value


@pytest.mark.core
@pytest.mark.connection
@pytest.mark.parametrize(
    "obj, correct",
    [
        (OptimizableType([0]), True),
        (Type(), False),
    ],
)
def test_is_connectable(obj, correct):
    assert OptimizableType([1, 2, 3]).is_connectable(obj) == correct


@pytest.mark.core
@pytest.mark.connection
@pytest.mark.parametrize(
    "value0, value1, same",
    [
        (None, None, True),
        ("", "", True),
        (1, 1, True),
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, 2, 3], False),
        (1, [1, 2, 3], False),
    ],
)
def test_create(value0, value1, same):
    t = OptimizableType(value0)
    assert t.is_same(value1) == same


