class Solution:
    def numSquares(self, n: int) -> int:  
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for s in range(1, int(sqrt(i)) + 1):
                dp[i] = min(dp[i], 1 + dp[i - (s * s)])
         
        return dp[-1]
                
            
            
            
            
        

            