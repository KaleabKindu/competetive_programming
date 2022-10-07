class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.total = sum(nums)
        n = len(nums)
        memo = {}
        def dp(i = 0, total = 0):
            if i >= n:
                return False
            if (i, total) in memo:
                return memo[(i, total)]
            if self.total - total <= total:
                return True if self.total - total == total else False
            memo[(i, total)] = dp(i + 1, total) or dp(i + 1, total + nums[i])
            return memo[(i, total)]
        return dp()
            