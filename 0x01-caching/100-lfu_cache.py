#!/usr/bin/env python3
""" LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class"""
    def __init__(self):
        """ Initialize LFUCache"""
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_items = [
                        k for k in self.cache_data
                        if self.freq[k] == min(self.freq.values())]
                if len(lfu_items) > 1:
                    lru_key = min(lfu_items, key=lambda x: self.freq[x])
                    del self.cache_data[lru_key]
                    del self.freq[lru_key]
                    print("DISCARD:", lru_key)
                else:
                    lfu_key = lfu_items[0]
                    del self.cache_data[lfu_key]
                    del self.freq[lfu_key]
                    print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            self.freq[key] = 0

        if key in self.freq:
            self.freq[key] += 1

    def get(self, key):
        """ Get an item by key"""
        if key is not None and key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data[key]
        return None
