#!/usr/bin/env python3
"""
Module contains the function index_range
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    if page <= 0:
        start = 0
    else:
        start = (page - 1) * page_size
    end = start + page_size
    return start, end
