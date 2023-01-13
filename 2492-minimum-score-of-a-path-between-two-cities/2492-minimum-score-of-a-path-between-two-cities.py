class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))
        
        answer = float('inf')
        visited = set()
        def dfs(node = 1):
            visited.add(node)
            for child, distance in graph[node]:
                if child not in visited:
                    dfs(child)
        
        
        dfs()
        for node in visited:
            for child, distance in graph[node]:
                answer = min(distance, answer)
        return answer