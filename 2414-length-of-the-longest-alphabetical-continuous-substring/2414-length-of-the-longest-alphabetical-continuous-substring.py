class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        longest = float('-inf')
        l, r = 0, 0
        previous = '`'
        while r < n:
            if ord(s[r]) == ord(previous) + 1:
                previous = s[r]
                r += 1
                longest = max(longest, r - l)
            else:
                l = r
                previous = chr(ord(s[l]) - 1)
        
        return longest
                