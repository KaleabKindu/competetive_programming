class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = -float('inf')
        temp = max
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxcount = temp(count, maxcount)
                count = 0
        maxcount = temp(count, maxcount)
        return maxcount