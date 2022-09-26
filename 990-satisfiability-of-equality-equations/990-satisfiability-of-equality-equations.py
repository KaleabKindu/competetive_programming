#   Quick Find Implementation
class UnionFind:
    def __init__(self):
        self.root = [i for i in range(26)]
        
    def find(self, x):
        x = ord(x) - 97
        return self.root[x]
        
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            for i in range(len(self.root)):
                if self.root[i] == yroot:
                    self.root[i] = xroot
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        UF = UnionFind()
        
        for equation in equations:
            x, operation, y = equation[0], equation[1:3], equation[-1]
            if operation == '==':
                UF.union(x, y)
        
        for equation in equations:
            x, operation, y = equation[0], equation[1:3], equation[-1]
            if operation == '!=':
                if UF.connected(x, y):
                    return False
        return True
            
            
        