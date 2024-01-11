#!/usr/bin/env python3
"""Defines duck typed function"""
from typing import Sequence, Any, Union, Optional

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Takes a sequence and returns the first element if the sequence is not empty, otherwise returns None.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence if it's not empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
