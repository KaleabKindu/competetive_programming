class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def dp(i = 1, j = n):
            if i >= j:
                return 1 
            subtrees = 0
            for k in range(i, j + 1):
                subtrees += dp(i, k - 1) * dp(k + 1, j)
                
            return subtrees 
        
        return dp() 
    
                
            
        
        
        
        
        
        
        
        

                
                