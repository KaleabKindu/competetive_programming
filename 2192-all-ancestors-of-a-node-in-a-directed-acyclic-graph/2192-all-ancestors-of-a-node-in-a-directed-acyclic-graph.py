class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        degree = {x: 0 for x in range(n)}
        for u, v in edges:
            graph[u].add(v)
            degree[v] += 1
        queue = deque()
        for i in range(n):
            if degree[i] == 0:
                queue.append(i)
        answer = [set() for _ in range(n)]
        while queue:
            cur = queue.popleft()
            for neighbor in graph[cur]:
                degree[neighbor] -= 1
                answer[neighbor].add(cur)
                answer[neighbor] = answer[neighbor].union(answer[cur])
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return [sorted(ancestor) for ancestor in answer]
        
        
       