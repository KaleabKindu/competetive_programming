class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for city_1, city_2 in connections:
            graph[city_1].add((True, city_2))
            graph[city_2].add((False, city_1))
        visited = [False]*(len(connections) + 1)
        flips = 0
        stack = [0]
        while stack:
            city = stack.pop()
            visited[city] = True
            for direction, child in graph[city]:
                if not visited[child]:
                    if direction:
                        flips += 1
                    stack.append(child)

        return flips
            