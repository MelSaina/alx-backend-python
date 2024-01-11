#!/usr/bin/env python3
"""Advanced type annotated function"""
from typing import Mapping, Any, TypeVar, Union, Optional

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely retrieves the value associated with the given key from the dictionary.
    If the key is not present, returns the default value.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to retrieve the value.
        default (Optional[T]): The default value to return if the key is not present (default is None).

    Returns:
        Union[Any, T]: The value associated with the key if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
