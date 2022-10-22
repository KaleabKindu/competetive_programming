class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n, m = len(mat), len(mat[0])
        k = 0
        while k < 4:
            for i in range(n):
                for j in range(i, m):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            for i in range(n):
                l = 0
                r = m - 1
                while l < r:
                    mat[i][l], mat[i][r] = mat[i][r], mat[i][l]
                    l += 1
                    r -= 1
            if mat == target:
                return True
            k += 1
        return False
        
        