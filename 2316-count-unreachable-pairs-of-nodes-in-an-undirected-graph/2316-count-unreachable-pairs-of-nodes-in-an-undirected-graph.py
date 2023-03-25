class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(child)
        components = []
        previous = len(visited)
        for node in range(n):
            if node not in visited:
                dfs(node)
                components.append(len(visited) - previous)
                previous = len(visited)
                
        prefix = []
        total = 0
        for num in components:
            total += num
            prefix.append(total)
            
        pairs = 0
        for i in range(1, len(components)):
            pairs += components[i]*prefix[i - 1]
            
        return pairs
                
