class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(set)
        degree = [0 for _ in range(n)]
        for node, child in edges:
            degree[node] += 1
            degree[child] += 1
            graph[node].add(child)
            graph[child].add(node)
            
        leaves = []   
        
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)
        
        while n > 2:
            n -= len(leaves)
            new_leaf = []
            while leaves:
                current = leaves.pop()
                for child in graph[current]:
                    graph[child].remove(current)
                    degree[child] -= 1
                    if degree[child] == 1:
                        new_leaf.append(child)
            leaves = new_leaf

        return leaves 
          

            
            
            
            
               