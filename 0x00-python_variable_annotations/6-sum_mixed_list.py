#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list mxd_lst of integers and floats and returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The list containing integers and floats.

    Returns:
        float: The sum of the integers and floats in the list.
    """
    return float(sum(mxd_lst))
