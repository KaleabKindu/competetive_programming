class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, s = len(s1), len(s2), len(s3)
        
        if n + m != s:
            return False
        
        @cache
        def dp(i = 0, j = 0):
            if i + j >= s:
                return True
            if i >= n:
                return s2[j:] == s3[i + j:]
            if j >= m:
                return s1[i:] == s3[i + j:]
            if s1[i] == s3[i + j] and s2[j] == s3[i + j]:
                return dp(i + 1, j) or dp(i, j + 1)
            elif s1[i] == s3[i + j]:
                return dp(i + 1, j)
            elif s2[j] == s3[i + j]:
                return dp(i, j + 1)
        
        return dp()
        
          
        