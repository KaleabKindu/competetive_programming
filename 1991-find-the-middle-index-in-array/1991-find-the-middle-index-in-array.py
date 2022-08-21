class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [_ for _ in nums]
        for i in range(1, len(nums)):
            prefix[i] += prefix[i - 1]
        
        suffix = [_ for _ in nums]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] += suffix[i + 1]
        
        for i in range(len(prefix)):
            if prefix[i] == suffix[i]:
                return i
        return -1