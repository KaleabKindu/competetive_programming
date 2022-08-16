class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.sum = 0
class MapSum:

    def __init__(self):
        self.map = {}
        self.root = Node()
        

    def insert(self, key: str, val: int) -> None:
        current = self.root
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        for char in key:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char] 
            current.sum += delta

    def sum(self, prefix: str) -> int:
        current = self.root
        for char in prefix:
            current = current.children[char]
        return current.sum
            
                


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)