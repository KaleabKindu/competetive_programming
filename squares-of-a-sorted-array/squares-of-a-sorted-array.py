class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        rng, length = range, len
        for i in rng(length(nums)):
            nums[i] *= nums[i]
        
        return sorted(nums)