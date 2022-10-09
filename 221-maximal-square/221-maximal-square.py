class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        
        @cache
        def dp(i, j):
            if not (0 <= i < n and 0 <= j < m):
                return 0
            if matrix[i][j] == '0':
                return 0
            down = dp(i + 1, j) + 1
            right = dp(i, j + 1) + 1
            diagonal = dp(i + 1, j + 1) + 1 
            
            return min(down, right, diagonal) 
        answer = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    answer = max(answer, dp(i, j)**2)
                    
        return answer