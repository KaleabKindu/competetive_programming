class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        self.total = sum(nums)
        if self.total & 1:
            return False
        n = len(nums)
        @cache
        def dp(i = 0, total = 0):
            if i >= n:
                return False
            if self.total - total <= total:
                return True if self.total - total == total else False
            if dp(i + 1, total):
                return True
            if dp(i + 1, total + nums[i]):
                return True
            return False
        
        return dp()
    
            
            