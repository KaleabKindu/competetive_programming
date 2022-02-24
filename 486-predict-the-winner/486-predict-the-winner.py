class Solution:
    

    def PredictTheWinner(self, nums: List[int]) -> bool:
        # @lru_cache()
        def helper(leftindex, rightindex):
            if leftindex==rightindex:
                return nums[leftindex]
            
            left = nums[leftindex] - helper(leftindex + 1, rightindex)
            
            right = nums[rightindex] - helper(leftindex, rightindex - 1)
            
            return max(left, right)
            
        return helper(0, len(nums)-1) >= 0 
      

        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#             if (leftindex,rightindex,turn) in memo:
#                 return memo[(leftindex,rightindex,turn)]
#             if  leftindex>rightindex:
#                 return p1 >= p2
#             if turn:
#                 left=helper(leftindex+1, rightindex, False, p1+nums[leftindex], p2,memo)
#                 right=helper(leftindex, rightindex-1, False, p1+nums[rightindex], p2,memo)
                
#                 memo[(leftindex,rightindex,turn)] = left or right
#                 print(memo)
#                 return left or right
#             else:
#                 left=helper(leftindex+1, rightindex, True, p1, p2+nums[leftindex],memo)
#                 right=helper(leftindex, rightindex-1,True, p1, p2+nums[rightindex], memo)
                
#                 memo[(leftindex,rightindex,turn)] = left and right
#                 return left and right
     
        

       
                
            
        