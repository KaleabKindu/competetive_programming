# Quick Union By Rank Implementation with Path Compression
class UnionFind:
    def __init__(self):
        self.root = [i for i in range(26)]
        self.rank = [0 for i in range(26)]
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y):
        x = ord(x) - 97
        y = ord(y) - 97
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            if self.rank[xroot] > self.rank[yroot]:
                self.root[yroot] = xroot
            elif self.rank[xroot] < self.rank[yroot]:
                self.root[xroot] = yroot
            else:
                self.root[yroot] = xroot
                self.rank[xroot] += 1
                
    def connected(self, x, y):
        x = ord(x) - 97
        y = ord(y) - 97
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
            
            
        