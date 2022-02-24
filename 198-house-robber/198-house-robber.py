class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache()
        def helper(index):
            if index==len(nums)-1:
                return nums[index]
            if index==len(nums)-2:
                return max(nums[index],nums[index+1])
            one=helper(index+1)
            two=helper(index+2)+nums[index]
            return max(one, two)  
        
        
        return helper(0)
       
            
            
        
        