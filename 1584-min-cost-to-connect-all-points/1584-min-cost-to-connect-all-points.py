class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class UnionFind:
    def __init__(self, points):
        self.root = {}
        for point in points:
            self.root[point] = point
        self.rank = {}
        for point in points:
            self.rank[point] = 0
    def find(self,node):
        if self.root[node] == node:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    def union(self,node1, node2):
        xr = self.find(node1)
        yr = self.find(node2)
        if xr != yr:
            if self.rank[xr] > self.rank[yr]:
                self.root[yr] = xr
            elif self.rank[xr] < self.rank[yr]:
                self.root[xr] = yr
            else:
                self.root[yr] = xr
                self.rank[xr] += 1
    def connected(self,node1, node2):
        return self.find(node1) == self.find(node2)
        
class Solution:
    def minCostConnectPoints(self, _points: List[List[int]]) -> int:
        
        points = []
        for x, y in _points:
            points.append(Node(x, y))
            
        
        edges = []
        for i in range(len(points)):
            xpoint_1, ypoint_1 = points[i].x, points[i].y
            for j in range(i + 1, len(points)):
                xpoint_2, ypoint_2 = points[j].x, points[j].y
                distance = abs(xpoint_1 - xpoint_2) + abs(ypoint_1 - ypoint_2)
                edges.append([distance, points[i], points[j]])
        
        edges = sorted(edges, key=lambda x:x[0])
        UF = UnionFind(points)
        n = len(_points)
        costs = 0
        count = 0
        while count < n - 1:
            for cost, node1, node2 in edges:
                if not UF.connected(node1, node2):
                    costs += cost
                    UF.union(node1, node2)
                    count += 1
        return costs