class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s)
        substring = set()
        substrings = 0
        l, r = 0, 0
        while r < n:
            if s[r] not in substring:
                substring.add(s[r])
                r += 1
            else:
                substrings += 1
                substring.clear()
                l = r
                
        return substrings + 1