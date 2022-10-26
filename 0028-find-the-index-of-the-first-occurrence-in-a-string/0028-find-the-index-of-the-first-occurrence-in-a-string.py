class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        prime = 31
        needle_hash = 0
        for i in range(m):
            needle_hash += (ord(needle[i]) - 96)*prime**i
        haystack_hash = 0
        l, r = 0, 0
        while r < n:
            if r - l + 1 <= m:
                haystack_hash += (ord(haystack[r]) - 96)*prime**(r - l)
                r += 1
                if r - l == m and haystack_hash == needle_hash:
                    return l
            else:
                haystack_hash -= (ord(haystack[l]) - 96)
                haystack_hash /= prime
                l += 1
                
        return -1
