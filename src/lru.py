#!/usr/bin/env python3
from typing import Any, Optional

class _Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key=None, val=None):
        self.key = key
        self.val= val
        self.prev: "_Node|None" = None
        self.next: "_Node|None" = None

class LRUCache:
    """
    A Least Recently Used (LRU) cache keeps items in the cache until it reaches its size
    and/or item limit (only item in our case). In which case, it removes an item that was accessed
    least recently.
    An item is considered accessed whenever `has`, `get`, or `set` is called with its key.

    Implement the LRU cache here and use the unit tests to check your implementation.
    """

    def __init__(self, item_limit: int):
        # TODO: implement this function
        if item_limit <=0:
            raise ValueError("item_limit must be >0")

        self.limit = item_limit
        self.map: dict[str, Node] = {}
        self.head = _Node()  # dummy head (MRU is head.next)
        self.tail = _Node()  # dummy tail (LRU is tail.prev)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def _add_mru(self, n: _Node) -> None:
        n.prev = self.head
        n.next = self.head.next 
        self.head.next.prev = n
        self.head.next = n
    
    def _remove(self, n: _Node) ->None:
        n.prev.next = n.next
        n.next.prev = n.prev
        n.prev = n.next = None

    def _touch(self, n: _Node) -> None:
        # gotta move to MRU
        self._remove(n)
        self._add_mru(n)
    
    def has(self, key: str) -> bool:
        # TODO: implement this function
        n = self.map.get(key)

        if not n:
                return False
        self._touch(n)
        return True

    def get(self, key: str) -> Optional[Any]:
        # TODO: implement this function
        n = self.map.get(key)
        if not n:
            return None
        self._touch(n)
        return n.val

    def set(self, key: str, value: Any):
        # TODO: implement this function
        if key in self.map:
            n = self.map[key]
            n.val = value
            self._touch(n)
            return
        n = _Node(key, value)
        self.map[key] = n
        self._add_mru(n)

        if len(self.map) >self.limit:
            # evict LRU 
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]
