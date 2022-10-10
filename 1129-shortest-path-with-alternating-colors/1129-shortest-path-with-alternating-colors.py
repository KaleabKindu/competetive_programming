class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for u, v in redEdges:
            graph[u].append((v, 'r'))
        for u, v in blueEdges:
            graph[u].append((v, 'b'))
            
        answer = [-1 for i in range(n)]
        
        def bfs():
            queue = deque([(0,'', 0)])
            visited = set([(0, '')])
            while queue:
                node, color, steps = queue.popleft()
                if answer[node] == -1:
                    answer[node] = steps
                for neighbor, n_color in graph[node]:
                    if n_color != color and (neighbor, n_color) not in visited:
                        visited.add((neighbor, n_color))
                        queue.append((neighbor, n_color, steps + 1))
            return -1
        bfs()
        
        return answer
                        
            
            
            