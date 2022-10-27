class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n + 1)]
        self.rank = [0 for i in range(n + 1)]
    def find(self,node1):
        if self.root[node1] == node1:
            return node1
        self.root[node1] = self.find(self.root[node1])
        return self.root[node1]
    def union(self,node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
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
        
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        Uf = UnionFind(n)
        for node_1, node_2 in edges:
            if not Uf.connected(node_1, node_2):
                Uf.union(node_1, node_2)
            else:
                return [node_1, node_2]
        