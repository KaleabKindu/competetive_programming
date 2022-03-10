class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        choice = prices[0]
        maxprofit = 0
        for price in prices:
            if price < choice:
                choice = price
            else:
                maxprofit = max(maxprofit, price - choice)
                
        return maxprofit
        
        
        
        
        
        
        
        
                
            
        