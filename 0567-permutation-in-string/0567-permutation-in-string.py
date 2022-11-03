class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s2), len(s1)
        substring = defaultdict(int)
        for char in s1:
            substring[char] += 1
        counter = defaultdict(int)
        l, r = 0, 0
        while r < n:
            if r - l + 1 <= m:
                counter[s2[r]] += 1
                r += 1
                if r - l == m:
                    if substring == counter:
                        return True
            else:
                counter[s2[l]] -= 1
                if counter[s2[l]] == 0:
                    counter.pop(s2[l])
                l += 1
        return False
                    