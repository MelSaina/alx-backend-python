#!/usr/bin/env python3
"""Type-annotated function make_multiplier"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as argument and returns a function that multiplies a float by multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float argument and returns the product of the argument and multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function

