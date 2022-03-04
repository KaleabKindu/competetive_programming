class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for src, des, w in times:
            graph[src].append((w, des))
            
        minHeap = [(0, k)]
        visited = set()
        t = 0
        while minHeap :
            weight, node = heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            t = weight
            for Nweight, neighbor in graph[node]:
                if neighbor not in visited:
                    heappush(minHeap, (weight + Nweight, neighbor))
        return t if len(visited) == n else -1