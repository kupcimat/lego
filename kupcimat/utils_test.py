from dataclasses import dataclass

from kupcimat.utils import field_names


@dataclass
class TestDataClass:
    a: str = "a"
    b: str = "b"
    c: str = "c"


def test_field_names():
    assert field_names(TestDataClass) == ["a", "b", "c"]
    assert field_names(TestDataClass()) == ["a", "b", "c"]
