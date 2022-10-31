class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        in_bound = lambda r, c: 0 <= r < n and 0 <= c < m
        
        queue = deque([(0, 0, 0)])
        visited = set()
        visited.add((0, 0, 0))
        steps = 0
        while queue:
            for i in range(len(queue)):
                r, c, obs = queue.popleft()
                if r == n - 1 and c == m - 1:
                    return steps
                if obs > k:
                    continue
                for direction in directions:
                    nr, nc = r + direction[0], c + direction[1]
                    if in_bound(nr, nc) and (nr, nc, obs + grid[nr][nc]) not in visited:
                        queue.append((nr, nc, obs + grid[nr][nc]))
                        visited.add((nr, nc, obs + grid[nr][nc]))
            steps += 1

        return -1
        
        