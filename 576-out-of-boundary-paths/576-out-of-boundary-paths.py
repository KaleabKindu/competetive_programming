class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        in_bound = lambda i, j: 0 <= i < m and 0 <= j < n
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        @cache 
        def dp(i = startRow, j = startColumn, moves = 0):
            if not in_bound(i, j):
                return 1
            if moves == maxMove:
                return 0
            temp = 0
            for direction in directions:
                temp += dp(i + direction[0], j + direction[1], moves + 1)
            return temp
        
        return dp() % (10**9 + 7)
        