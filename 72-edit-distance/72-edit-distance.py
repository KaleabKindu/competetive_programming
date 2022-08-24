class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        possibility = [(0, 1), (1, 1), (1, 0)]
        
        @lru_cache(None)
        def dp(i = 0, j = 0):
            if j >= len(word2):
                return len(word1) - i
            if i >= len(word1):
                return len(word2) - j
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            answer = float('inf')
            for pos in possibility:
                newi, newj = i + pos[0], j + pos[1]
                answer = min(answer, 1 + dp(newi, newj))
            return answer
        
        return dp()