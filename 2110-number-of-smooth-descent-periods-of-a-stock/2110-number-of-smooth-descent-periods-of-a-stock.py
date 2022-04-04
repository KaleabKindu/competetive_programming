class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = [1 for _ in prices]
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] - prices[i + 1] == 1:
                dp[i] += dp[i + 1]
        
        return sum(dp)
            