class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ""
        
        for k in range(len(s)):
            i, j = k, k
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > len(substring):
                    substring = s[i: j + 1]
                i -= 1
                j += 1
            i, j = k - 1, k
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > len(substring):
                    substring = s[i: j + 1]
                i -= 1
                j += 1
        return substring