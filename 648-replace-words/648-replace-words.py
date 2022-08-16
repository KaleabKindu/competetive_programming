class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.root = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_node = current = Node()
        def findRoot(target):
            current = root_node
            prefix = []
            for char in target:
                if current.root:
                    return "".join(prefix)
                if char not in current.children:
                    return ""
                prefix.append(char)
                current = current.children[char]
            return "".join(prefix) if current.root else ""
        
#       Trie insertion 
        for root in dictionary:
            for char in root:
                if char not in current.children:
                    current.children[char] = Node()
                current = current.children[char]
            current.root = True
            current = root_node

#       Replacement 
        sentence = sentence.split(" ")
        replacement = []
        for word in sentence:
            root = findRoot(word)
            if root:
                replacement.append(root)
            else:
                replacement.append(word)
                  
        return " ".join(replacement)
            
        
            
            