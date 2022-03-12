class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        @lru_cache()
        def dfs(rw, col):
            
            if rw == R - 1 and col == C - 1:
                return grid[rw][col]
            
            right = dfs(rw, col + 1) if col + 1 < C else float("inf")
            
            down = dfs(rw + 1, col) if rw + 1 < R else float("inf")
            
            
            return grid[rw][col] + min(right, down)
        
        return dfs(0, 0)