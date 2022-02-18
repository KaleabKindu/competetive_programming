class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1 for i in nums]
        prefixsum=1
        for i in range(len(nums)):
            output[i]=prefixsum
            prefixsum*=nums[i]
        postfixsum=1
        for i in range(len(nums)-1,-1,-1):
            output[i]*=postfixsum
            postfixsum*=nums[i]
        return output
        
        