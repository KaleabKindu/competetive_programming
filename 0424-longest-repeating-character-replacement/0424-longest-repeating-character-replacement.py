class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        answer = float('-inf')
        count = {char: 0 for char in s}
        l, r = 0, 0
        while r < n:
            replace = (r - l) - max(count.values())
            if replace <= k:
                count[s[r]] += 1
                r += 1
                if (r - l) - max(count.values()) <= k: 
                    answer = max(answer, r - l)
            else:
                count[s[l]] -= 1
                l += 1
        return answer