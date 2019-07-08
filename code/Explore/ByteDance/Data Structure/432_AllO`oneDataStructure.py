# Python Doubly Linked List beats 94% (32ms)
# reference: https://leetcode.com/problems/all-oone-data-structure/discuss/91430/Python-Doubly-Linked-List-beats-94-(32ms)
# TODO AC the problem
class Node:

    def __init__(self, value, next, prev, key):
        self.next = next
        self.prev = prev
        self.value = value
        self.keys = {key}


class DoubleList:

    def __init__(self):
        self.head = Node(-1, None, None, "")
        self.tail = Node(-1, None, None, "")
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertAfter(self, n, val, key):
        nn = Node(val, n.next, n, key)
        n.next = nn
        nn.next.prev = nn
        return nn

    def remove(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev
        del n


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll = DoubleList()
        self.keys = {}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.keys:
            n = self.dll.insertAfter(self.dll.head, 0, key)
            self.keys[key] = n
        else:
            n = self.keys[key]

        if n.value + 1 == n.next.value:
            # merge with next
            self.keys[key] = n.next
            n.keys.remove(key)
            n.next.keys.add(key)
        elif len(n.keys) == 1:
            # increment in place
            n.value += 1
        else:
            # insert new node
            nn = self.dll.insertAfter(n, n.value + 1, key)
            self.keys[key] = nn
            n.keys.remove(key)

            # Garbage collection
        if len(n.keys) <= 0:
            self.dll.remove(n)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.keys:
            return
        else:
            n = self.keys[key]

        if n.value == 1:
            # remove key/node
            del self.keys[key]
            n.keys.remove(key)
        elif n.value - 1 == n.prev.value:
            # merge with previous
            self.keys[key] = n.prev
            n.keys.remove(key)
            n.prev.keys.add(key)
        elif len(n.keys) == 1:
            # decrement in place
            n.value -= 1
        else:
            # insert new node
            nn = self.dll.insertAfter(n.prev, n.value - 1, key)
            n.keys.remove(key)
            self.keys[key] = nn

            # Garbage collection
        if len(n.keys) <= 0:
            self.dll.remove(n)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.dll.head.next.value == -1:
            return ""
        for k in self.dll.tail.prev.keys:
            # break
            return k

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.dll.head.next.value == -1:
            return ""
        for k in self.dll.head.next.keys:
            break
        return k