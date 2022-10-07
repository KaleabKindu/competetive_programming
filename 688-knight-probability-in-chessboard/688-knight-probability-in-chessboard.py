class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        in_bound = lambda i, j: 0 <= i < n and 0 <= j < n
        
        directions = [[1,2],[-1,2],[1,-2],[-1,-2],[-2,1],[-2,-1],[2,-1],[2,1]]
        
        @cache
        def dp(i = row, j = column, steps = 0):
            if steps == k:
                return 1 if in_bound(i, j) else 0
            if not in_bound(i, j):
                return 0
            temp = 0
            for direction in directions:
                temp += dp(i + direction[0], j + direction[1], steps + 1)
            return temp
        return dp() / (8 ** k)