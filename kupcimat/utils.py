from dataclasses import fields
from itertools import chain
from typing import Any, List, TypeVar

T = TypeVar("T")


def field_names(class_or_instance: Any) -> List[str]:
    return [field.name for field in fields(class_or_instance)]


def flatten(list_of_lists: List[List[T]]) -> List[T]:
    return list(chain.from_iterable(list_of_lists))
