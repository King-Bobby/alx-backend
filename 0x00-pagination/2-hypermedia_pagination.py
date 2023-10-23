#!/usr/bin/env python3
"""Module for 2-hypermedia_pagination.py"""


import csv
import math
from typing import List, Tuple, Dict, Union


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets the page required"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data) or start < 0 or end < 0:
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str,
                                               Union[int, List[List], None]]:
        """returns a dictionary containing key-value pairs"""
        page_data = self.get_page(page, page_size)
        next_page_data = self.get_page(page + 1, page_size)
        return {
                "page_size": len(page_data),
                "page": page,
                "data": page_data,
                "next_page": page + 1 if next_page_data else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": math.ceil(len(self.dataset()) / page_size)
                }
