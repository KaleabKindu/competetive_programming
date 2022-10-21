class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        while i < n:
            count = 1
            j = i + 1
            while j < n and nums[i] == nums[j]:
                count += 1
                j += 1
            if count < 3:
                return nums[i]
            i = j
            
        
            
            
            
            