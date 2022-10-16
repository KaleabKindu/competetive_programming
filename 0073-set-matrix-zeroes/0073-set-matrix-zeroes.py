class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        zeros = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeros.add((i, j))
                    
        for r, c in zeros:
            for k in range(m):
                matrix[r][k] = 0
            for k in range(n):
                matrix[k][c] = 0
                        
                        