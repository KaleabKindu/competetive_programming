class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        graph = defaultdict(list)
        
        for i, node in enumerate(edges):
            if node != -1:
                graph[i].append(node)
        visited = [False for _ in range(n)]
        queue = deque([(node1, 0)])
        visited[node1] = True
        targets = defaultdict(int)
        while queue:
            node, distance = queue.popleft()
            targets[node] = distance
            for child in graph[node]:
                if not visited[child]:
                    queue.append((child, distance + 1))
                    visited[child] = True
        answer = []
                    
        visited = [False for _ in range(n)]
        queue = deque([(node2, 0)])
        visited[node2] = True
        while queue:
            node, distance = queue.popleft()
            if node in targets:
                temp = max(distance, targets[node])
                heappush(answer, (temp, node))
            for child in graph[node]:
                if not visited[child]:
                    queue.append((child, distance + 1))
                    visited[child] = True
                    
        return answer[0][1] if answer else -1