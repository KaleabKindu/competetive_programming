class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        in_bound = lambda i, j: 0 <= i < n and 0 <= j < m
        
        @cache
        def dp(i = 0, j = 0):
            if not in_bound(i, j):
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0
            
            if i == n - 1 and j == m - 1:
                return 1
            
            down = dp(i + 1, j)
            
            right = dp(i, j + 1)
            
            return down + right
        return dp()
            