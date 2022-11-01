class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        in_bound = lambda r, c: 0 <= r < n and 0 <= c < m
        
        visited = [[False] * m for i in range(n)]
        
        @cache
        def dfs(i, j):
            visited[i][j] = True
            res = 1
            for direction in directions:
                r, c = i + direction[0], j + direction[1]
                if in_bound(r, c) and not visited[r][c] and grid[i][j] < grid[r][c]:
                    res += dfs(r, c)
            visited[i][j] = False
            return res
        answer =  0
        for i in range(n):
            for j in range(m):
                answer += dfs(i, j)
        return answer % (10**9 + 7)