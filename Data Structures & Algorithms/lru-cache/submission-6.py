class Node:
        def __init__(self, key:int, val: int, nextNode = None, prevNode = None) -> None:
            self.key = key
            self.val =val
            self.next = nextNode
            self.prev = prevNode

class LRUCache:
            
    def __init__(self, capacity: int):
        self.lookup = {}
        self.capacity = capacity
        self.LRU = Node(0,0)
        self.MRU = Node(0,0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def get(self, key: int) -> int:
        if key in self.lookup:
            self.remove(self.lookup[key])
            self.insert(self.lookup[key])
            return self.lookup[key].val
        return -1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, n):
        self.MRU.prev.next = n
        n.prev = self.MRU.prev
        n.next = self.MRU
        self.MRU.prev = n

    def put(self, key: int, value: int) -> None:
        if key not in self.lookup:
            if self.capacity <= len(self.lookup):
                lru_node = self.LRU.next
                self.remove(lru_node)
                del self.lookup[lru_node.key]
            n = Node(key, value)
            self.lookup[key] = n
            self.insert(n)
        else:
            self.lookup[key].val = value
            n = self.lookup[key]
            self.remove(n)
            self.insert(n)
