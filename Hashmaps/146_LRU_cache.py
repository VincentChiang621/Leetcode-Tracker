# Time: O(n)
# Space: O(n) 
# linked list + hashmap to implement LRU cache; also left and right more used Nodes for deletion
class Node:
        def __init__(self, key, val):
            self.key, self.val = key, val
            self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}  # map key to Nodes
        self.capacity = capacity

        # left is least used, right is most used
        self.left = self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])        
        self.hashmap[key] = Node(key, value)
        self.insert(self.hashmap[key])

        if len(self.hashmap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]