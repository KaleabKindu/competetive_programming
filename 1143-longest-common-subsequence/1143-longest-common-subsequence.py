class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(None)
        def dp(i = 0, j = 0):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]: 
                return 1 + dp(i + 1, j + 1)
            else:
                return max(dp(i + 1, j), dp(i, j + 1))
        
        
        return dp()