class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        
        def targetsum(index, summ = 0):
            if (index, summ) in dp:
                return dp[(index, summ)]
            if index >= len(nums):
                return 1 if summ == target else 0
            
            
            positive = targetsum(index + 1, nums[index] + summ)
            
            negative = targetsum(index + 1, -nums[index] + summ)
            
            dp[(index, summ)] = positive + negative
            return dp[(index, summ)]
        return targetsum(0)
                