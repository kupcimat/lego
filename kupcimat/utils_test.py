import pytest
from dataclasses import dataclass

from kupcimat.utils import field_names, flatten


@dataclass
class TestDataClass:
    a: str = "a"
    b: str = "b"
    c: str = "c"


@pytest.mark.parametrize(
    "input,expected",
    [(TestDataClass, ["a", "b", "c"]), (TestDataClass(), ["a", "b", "c"])],
)
def test_field_names(input, expected):
    assert field_names(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ([], []),
        ([[]], []),
        ([[], []], []),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[1, 2, 3], []], [1, 2, 3]),
        ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 4, 5, 6]),
    ],
)
def test_flatten(input, expected):
    assert flatten(input) == expected
