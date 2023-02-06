class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        m = len(pref)
        answer = 0
        for word in words:
            n = len(word)
            i, j = 0, 0
            while i < n and j < m:
                if word[i] != pref[j]:
                    break
                i += 1
                j += 1
            if j == m:
                answer += 1
        return answer
            