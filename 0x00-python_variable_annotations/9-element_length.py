#!/usr/bin/env python3
"""Type-annotated function element_length"""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list of sequences and returns a list of tuples, where each tuple contains an element from the input list
    and its corresponding length.

    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains an element from the input list
        and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
