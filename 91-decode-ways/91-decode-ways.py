class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def dp(index = 0):
            if index >= len(s):
                return 1 if index == len(s) else 0
            if s[index] == '0':
                return 0
            one = dp(index + 1) 
            two = dp(index + 2) if index + 1 < len(s) and int(s[index] + s[index + 1]) <= 26 else 0
            return one + two
        return dp()