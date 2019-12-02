# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

from collections import OrderedDict

class LRUCache:
    # create an ordered dictionary that can store up to capacity key-value pairs
    def __init__(self, capacity):
        self.od = OrderedDict()
        self.cap = capacity
    # when getting a key-value pair, move it to the end of the dictionary and return the key
    def get(self, key):
        if key in self.od:
            print("found key")
            val = self.od[key]
            self.od.pop(key)
            self.od[key] = val
            return val
        else:
            print("key is missing")
            return -1
    # when adding a key-value pair, add it to the dictionary and delete the first entry
    def put(self, key, value):
        if key in self.od:
            self.od.pop(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            for k in self.od:
                self.od.pop(k)
                break
    # print the key-value pairs currently stored in the cache
    def show(self):
        print(self.od)
