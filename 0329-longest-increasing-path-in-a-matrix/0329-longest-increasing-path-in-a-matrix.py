class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        in_bound = lambda r, c: 0 <= r < n and 0 <= c < m
        
        visited = [[False] * m for i in range(n)]
        
        @cache
        def dfs(i, j):
            visited[i][j] = True
            res = 0
            for direction in directions:
                r, c = i + direction[0], j + direction[1]
                if in_bound(r, c) and not visited[r][c] and matrix[i][j] < matrix[r][c]:
                    res = max(res, dfs(r, c))
            visited[i][j] = False
            return 1 + res
        answer =  0
        for i in range(n):
            for j in range(m):
                answer = max(answer, dfs(i, j))
        return answer