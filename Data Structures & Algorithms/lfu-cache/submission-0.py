class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    # adding new node to this freq list
    def append(self, node):
        prev_node = self.tail.prev
        next_node = self.tail
        node.next = next_node
        node.prev = prev_node
        prev_node.next = node
        self.tail.prev = node
        self._size += 1

    # remove from current freq linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self._size -= 1

    # remove from front - LRU with same freq
    def pop_left(self):
        if self._size == 0: return None
        node = self.head.next
        self.remove(node)
        return node

    def is_empty(self):
        return self._size == 0
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_map = {}
        self.freq_map = {}
        self.hash_map = defaultdict(DoublyLinkedList) 

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1

        node = self.key_map[key]
        freq = self.freq_map[key]
        self.hash_map[freq].remove(node)
        if self.hash_map[freq].is_empty() and freq == self.min_freq:
            self.min_freq += 1
            
        self.hash_map[freq + 1].append(node)
        self.freq_map[key] = freq + 1


        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0: return

        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self.get(key)
            return

        if len(self.key_map) >= self.capacity:
            old_node = self.hash_map[self.min_freq].pop_left()
            del self.freq_map[old_node.key]
            del self.key_map[old_node.key]

        node = ListNode(key, value)
        self.key_map[key] = node
        self.freq_map[key] = 1
        self.hash_map[1].append(node)
        self.min_freq = 1