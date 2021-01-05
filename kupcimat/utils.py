from dataclasses import fields
from typing import Any, List


def field_names(class_or_instance: Any) -> List[str]:
    return [field.name for field in fields(class_or_instance)]


def flatten(list_of_lists: List[Any]):
    return [item for sublist in list_of_lists for item in sublist]
