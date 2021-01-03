from dataclasses import fields
from typing import Any, List


def field_names(class_or_instance: Any) -> List[str]:
    return [field.name for field in fields(class_or_instance)]
