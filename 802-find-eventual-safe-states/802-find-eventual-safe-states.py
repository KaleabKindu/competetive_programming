class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        path = set()
        def dfs(node):
            if node in path:
                return False
            path.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor): return False
            graph[node] = []
            path.remove(node)
            return True
        safe = set([_ for _ in range(len(graph))])
        for i in range(len(graph)):
               if not dfs(i): safe.remove(i)
        return safe
            
            