#!/usr/bin/env python3
"""Type-annotated function sum_list"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sums up a list of floats.

    Args:
        input_list (List[float]): The list of floats to be summed.

    Returns:
        float: The sum of the input_list.
    """
    return sum(input_list)
