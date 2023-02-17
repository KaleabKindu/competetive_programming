

class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.Dict = {}
        self.head, self.tail = ListNode(0,0), ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail

    def get(self, key: int) -> int:
        if key in self.Dict:
            self.remove(self.Dict[key])
            self.insert(self.Dict[key])
            return self.Dict[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.Dict:
            self.remove(self.Dict[key])
        temp = ListNode(key, value)
        self.Dict[key] = temp
        self.insert(temp)
        if len(self.Dict) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.Dict[lru.key]