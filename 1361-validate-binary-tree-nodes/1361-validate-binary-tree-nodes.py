from math import ceil
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    def find(self, node):
        if self.root[node] == node:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    def union(self, node1, node2):
        root1 = self.root[node1]
        root2 = self.root[node2]
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1
        
    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)
    def connectivity(self,n):
        root = 0
        for i in range(n):
            if self.root[i] == i:
                root += 1
        return root == 1 
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        UF = UnionFind(n)
        parent = defaultdict(int)
        for i in range(n):
            left, right = leftChild[i], rightChild[i]
            if left >= 0:
                parent[left] += 1
                if UF.connected(i,left):
                    return False
                UF.union(i, left)
            if right >= 0:
                parent[right] += 1
                if UF.connected(i,right):
                    return False
                UF.union(right, i)  
        root, nodes = 0, 0
        for i in range(n):
            if UF.root[i] == i:
                root += 1
            if parent[i] == 1:
                nodes += 1
            
        return root == 1 and nodes == n - 1
                