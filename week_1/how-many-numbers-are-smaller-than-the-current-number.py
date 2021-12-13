class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[0 for _ in nums]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]>nums[j]:
                    count[i]+=1
                elif nums[i] == nums[j]:
                    continue
                else:
                    count[j]+=1
        return count
                    
            
