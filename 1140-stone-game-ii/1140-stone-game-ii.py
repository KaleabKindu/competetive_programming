class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        reward = sum(piles)
        for i in range(1, n):
            piles[i] = piles[i - 1] + piles[i]
        @cache
        def dp(i = 0, m = 1):
            if i >= n:
                return 0
            score = -float('inf')
            for x in range(1, min((2 * m) + 1, n - i + 1)):
                points = piles[i + x - 1] - piles[i - 1] if i > 0 else piles[i + x - 1]
                score = max(score, points - dp(i + x, max(m, x))) 
            return score
        
        winning_margin = dp()
        
        return (reward + winning_margin)//2
        
                