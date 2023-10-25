#!/usr/bin/env python3
"""Module contains the class LRUCache"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """class LRUCache"""
    def __init__(self):
        """initializes the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """returns key value"""
        if key is not None or item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_used = self.order.pop(0)
                del self.cache_data[lru_used]
                print("DISCARD:", lru_used)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """gets the item value for the key"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
