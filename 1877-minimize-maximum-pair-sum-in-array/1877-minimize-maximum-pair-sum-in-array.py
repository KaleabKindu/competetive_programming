class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxx=0
        start=0
        end=len(nums)-1
        while start<end:
            maxx=max(maxx,nums[start]+nums[end])
            start+=1
            end-=1
        return maxx
        
        