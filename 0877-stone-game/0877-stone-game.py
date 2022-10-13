class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        @cache
        def dp(i = 0, j = n - 1):
            if i > j:
                return  0
            front = piles[i] - dp(i + 1, j)
            end = piles[j] - dp(i, j - 1)
            return max(front, end)
        return dp() > 0
            