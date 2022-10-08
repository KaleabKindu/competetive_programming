class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        memo = {}
        def subsequence(word):
            m = len(word)
            l, r = 0, 0
            while l < n and r < m:
                if s[l] == word[r]:
                    l += 1
                    r += 1
                else:
                    l += 1
            memo[word] = r == m
            return memo[word]
        count = 0
        for word in words:
            if word not in memo:
                if subsequence(word):
                    count += 1
            elif memo[word]: count += 1
                
        return count
            