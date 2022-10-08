class UnionFind:
    def __init__(self, n):
        self.root = {i:i for i in range(1, n + 1)}
        self.rank = {i:0 for i in range(1, n + 1)}
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
    
    def traversable(self, n):
        temp = set()
        for i in range(1, n):
            temp.add(self.find(i))
        return len(temp) == 1
            

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        removed_edges = 0
        for _type, u, v in edges:
            if _type == 3:
                if not alice.connected(u,v) and not bob.connected(u,v):
                    alice.union(u,v)
                    bob.union(u,v)
                else: removed_edges += 1
        for _type, u, v in edges:
            if _type == 1:
                if alice.connected(u,v):
                    removed_edges += 1
                alice.union(u,v)
            if _type == 2:
                if bob.connected(u,v):
                    removed_edges +=1
                bob.union(u,v)
                
        return removed_edges if alice.traversable(n) and bob.traversable(n) else -1
            
                
            
        