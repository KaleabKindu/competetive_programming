class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0 for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            degree[v] += 1
        
        temp = sorted(graph,key=lambda x: degree[x])
        visited = set()
        def dfs(node):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(child)
        answer = []
        for node in temp:
            answer.append(node)
            if node not in visited:
                dfs(node)
            if len(visited) == n:
                break
        return answer
            