#!/usr/bin/env python3
"""Module contains the class FIFOCache"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOcache"""
    def __init__(self):
        """initialises the class"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """put an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.cache_order:
                    removed_key = self.cache_order[0]
                    self.cache_order.pop(0)
                    del self.cache_data[removed_key]
                    print("DISCARD:", removed_key)
            self.cache_data[key] = item
            self.cache_order.append(key)

    def get(self, key):
        """gets the key value"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
