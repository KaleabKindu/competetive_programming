class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0 for i in range(n)]
        i, j = 0, 1
        while j < n:
            if s[i] == s[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i - 1]
        max_len = lps[-1]
        index = lps.index(max_len)
        
        return s[index - (max_len - 1): index + 1]