class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        n, m, s = len(s1), len(s2), len(s3)
        @cache
        def dp(i = 0, j = 0):
            k = i + j
            if k >= s:
                return True
            if i < n and j < m and s1[i] == s3[k] and s2[j] == s3[k]:
                return dp(i + 1, j) or dp(i, j + 1)
            elif i < n and s1[i] == s3[k]:
                return dp(i + 1, j)
            elif j < m and s2[j] == s3[k]:
                return dp(i, j + 1)
        
        return dp()
        
          
        