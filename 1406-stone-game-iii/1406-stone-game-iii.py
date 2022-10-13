class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        for i in range(1, n):
            stoneValue[i] = stoneValue[i - 1] + stoneValue[i]
            
        @cache
        def dp(i = 0):
            if i >= n:
                return 0
            score = -float('inf')
            for stones in range(1, min(4, n - i + 1)):
                points = stoneValue[i + stones - 1] - stoneValue[i - 1] if i > 0 else stoneValue[i + stones - 1]
                score = max(score, points - dp(i + stones))
            return score
        
        verdict = dp()
        
        if verdict > 0:
            return 'Alice'
        elif verdict < 0:
            return 'Bob'
        else:
            return 'Tie'
        