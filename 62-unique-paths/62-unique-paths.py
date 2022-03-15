class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        dp = {}
        def path(m, n):
            if (m, n) in dp:
                return dp[(m, n)]
            if m == 0 or n == 0:
                return 0
            if m == 1 and n == 1:
                return 1
            dp[(m, n)] = path(m - 1, n) + path(m, n - 1)
            return dp[(m, n)]
        return path(m, n)