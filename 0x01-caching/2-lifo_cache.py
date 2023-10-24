#!/usr/bin/env python3
"""Module contains the Class LIFOCache"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache"""
    def __init__(self):
        """initialises the class"""
        super().__init__()

    def put(self, key, item):
        """puts an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print("DISCARD:", last_key)
            self.cache_data[key] = item

    def get(self, key):
        """gets the key value"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
