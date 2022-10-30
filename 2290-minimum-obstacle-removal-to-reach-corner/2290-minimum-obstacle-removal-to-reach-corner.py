class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        in_bound = lambda r, c: 0 <= r < n and 0 <= c < m
        
        
        heap = [(0, 0, 0)] # row, col, obstacles
        heapify(heap)
        best = [[float('inf')] * m for i in range(n)]
        
        while heap:
            obs, r, c = heappop(heap)
            if r == n - 1 and c == m - 1:
                return obs
            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]
                if in_bound(nr, nc):
                    weight = obs + grid[nr][nc]
                    if weight < best[nr][nc]:
                        best[nr][nc] = weight
                        heappush(heap, (weight, nr, nc))

        
        