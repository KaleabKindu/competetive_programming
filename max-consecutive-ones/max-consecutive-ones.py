class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = -float('inf')
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxcount = max(count, maxcount)
                count = 0
        maxcount = max(count, maxcount)
        return maxcount