class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        previousCount=0
        previousNum=None
        for i in range(len(nums)):
            if previousNum==None:
                previousNum=nums[i]+previousCount
                continue
            elif nums[i]<=previousNum:
                previousCount+=previousNum-nums[i]+1
                previousNum+=1
            else:
                previousNum=nums[i]
        return previousCount