class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=[0 for i in nums]
        for i in range(len(nums)):
            res[(i+k)%len(nums)]=nums[i]
        for i in range(len(nums)):
            nums[i]=res[i]
            
            
        
                
            
        
        