#!/usr/bin/env python3
"""Module contains the class MRUCache"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class MRUCache"""
    def __init__(self):
        """initializes the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """assigns a value for a key"""
        if key is not None or item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop(0)
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.order.insert(0, key)

    def get(self, key):
        """gets the item value for a key"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.insert(0, key)
        return self.cache_data[key]
