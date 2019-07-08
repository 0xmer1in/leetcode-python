# Python Dict + Double LinkedList
# reference: https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList
class Node:

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def set(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


# added a double linked list class to sparate out the double linked list operations
class Node:

    def __init__(self, k, v):
        self.next = None
        self.prev = None
        self.k = k
        self.v = v


class DLList:

    def __init__(self):
        self.size = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, n1, n2):
        assert n1 and n2
        n3  = n1.next
        # update pointers
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev  =prev
        node.prev, node.next = None, None

    def move_to_end(self, node):
        self.remove(node)
        self.insert_after(self.tail.prev, node)

    def add_to_end(self, node):
        self.insert_after(self.tail.prev, node)

    def remove_from_head(self):
        delete = self.head.next
        self.remove(delete)
        return delete.k


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.dll = DLList()
        self.size = 0

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        self.dll.move_to_end(node)
        return node.v

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if not node:
            node = Node(key, value)
            if self.size + 1 > self.capacity:
                delete_key = self.dll.remove_from_head()
                del self.map[delete_key]
            else:
                self.size += 1
            self.dll.add_to_end(node)
        else:
            node.v = value
            self.dll.move_to_end(node)
        self.map[key] = node