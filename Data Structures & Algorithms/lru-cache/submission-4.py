class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node

        # left=LRU, right=MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node

        node.prev = prev
        node.next = self.right


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from the list & delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

