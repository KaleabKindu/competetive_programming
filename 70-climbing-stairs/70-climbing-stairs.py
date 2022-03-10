class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n not in memo:
            if n < 2 :
                memo[n] = 1 
            else:
                memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return memo[n]
        
            
            