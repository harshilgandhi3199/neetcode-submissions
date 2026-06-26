class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            return

        node = Node(key, value)
        if len(self.hash_map) == self.capacity:
            lru_node = self.head.next
            self.remove(lru_node)
            del self.hash_map[lru_node.key]
        
        self.insert(node)
        self.hash_map[node.key] = node
            


        
