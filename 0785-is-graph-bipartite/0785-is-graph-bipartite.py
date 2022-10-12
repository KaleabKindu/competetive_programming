class Solution:
    def isBipartite(self, _graph: List[List[int]]) -> bool:
        graph = defaultdict(list)
        n = len(_graph)
        for u in range(n):
            for v in _graph[u]:
                graph[u].append(v)
                graph[v].append(u)
                
        def bipartite_bfs(cur):
            queue = deque([(cur,'r')])
            red = set([cur])
            blue = set()
            while queue:
                node, color = queue.popleft()
                for neighbor in graph[node]:
                    if color == 'r':
                        if neighbor in red:
                            return False
                        if neighbor not in blue:
                            blue.add(neighbor)
                            queue.append((neighbor, 'b'))
                    else:
                        if neighbor in blue:
                            return False
                        if neighbor not in red:
                            red.add(neighbor)
                            queue.append((neighbor, 'r'))
            return True
        
        for i in range(n):
            if not bipartite_bfs(i):
                return False
        return True
        
        
        