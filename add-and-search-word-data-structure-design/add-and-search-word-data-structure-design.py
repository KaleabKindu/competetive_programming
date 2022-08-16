class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.word = True
        

    def search(self, word: str) -> bool:
        def dfs(node = self.root, index = 0):
            current = node
            for i in range(index, len(word)):
                char = word[i]
                if char == '.':
                    for child in current.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False

                elif char not in current.children:
                    return False
                current = current.children[char]

            return current.word
        return dfs()
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)