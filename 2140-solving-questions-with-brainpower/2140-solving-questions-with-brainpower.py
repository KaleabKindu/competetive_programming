class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        
        @lru_cache(None)
        def dp(index = 0):
            if index >= len(questions):
                return 0
            solve = questions[index][0] + dp(index + questions[index][1] + 1) 
            
            skip = dp(index + 1)
            
            return max(solve, skip)
        
        return dp()
        