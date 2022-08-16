class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.word = False
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = current = Node()
        
        @lru_cache(None)
        def search(word, index = 0):
            current = root
            for i in range(index, len(word)):
                if current.word:
                    if search(word, i):
                        return True
                if s[i] not in current.children:
                    return False
                current = current.children[s[i]]
            return current.word
                
        
#         Trie Insertion
        
        for word in wordDict:
            for char in word:
                if char not in current.children:
                    current.children[char] = Node()
                current = current.children[char]
            current.word = True
            current = root
        
#         Trie Break
        return search(s)
        
        
                