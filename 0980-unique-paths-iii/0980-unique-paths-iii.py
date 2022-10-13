class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        in_bound = lambda i, j: 0 <= i < n and 0 <= j < m
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        self.emptycells = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    self.emptycells += 1
        visited = [[False]*m for i in range(n)]
        def dp(i, j, empty = 0):
            if grid[i][j] == -1:
                return 0
            if grid[i][j] == 2:
                return 1 if empty == self.emptycells else 0
            paths = 0
            for direction in directions:
                r, c = i + direction[0], j + direction[1]
                if in_bound(r, c) and not visited[r][c]:
                    visited[r][c] = True
                    paths += dp(r, c, empty + 1 if grid[r][c] == 0 else empty)
                    visited[r][c] = False
            return paths
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    visited[i][j] = True
                    return dp(i, j)
            
            
            