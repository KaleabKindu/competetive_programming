class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        dp = {}
        
        def BTBS(index, buying):
            if index >= len(prices):
                return 0
            if (index, buying) in dp:
                return dp[(index, buying)]
            if buying:
                buy = BTBS(index + 1, not buying) - prices[index]
                cooldown = BTBS(index + 1, buying) 
                dp[(index, buying)] = max(buy, cooldown)
            else:
                sell = BTBS(index + 2, not buying) + prices[index]
                cooldown = BTBS(index + 1, buying) 
                dp[(index, buying)] = max(sell, cooldown)
            return dp[(index, buying)]
        
        return BTBS(0, True)