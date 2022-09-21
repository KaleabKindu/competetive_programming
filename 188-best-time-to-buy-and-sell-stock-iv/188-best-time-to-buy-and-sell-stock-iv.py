class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)   
        @lru_cache(None)
        def dp(i = 0, bought = False, transactions = k):
            if i >= n:
                return 0
            if transactions <= 0:
                return 0
            profit = dp(i + 1, bought, transactions)
            if not bought:
                return max(profit, -prices[i] + dp(i + 1, True, transactions))
            else:
                return max(profit, prices[i] + dp(i + 1, False, transactions - 1))
        
        return dp()
                    
                        
        
        
        
        
        
        
        
