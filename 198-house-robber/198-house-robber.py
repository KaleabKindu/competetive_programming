class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        @lru_cache()
        def dfs(index):
            if index > len(nums) - 1:
                return 0
            if index == len(nums) - 1:
                return nums[index]
            
            steal = nums[index] + dfs(index + 2)
            
            Nsteal = dfs(index + 1)
            
            return  max(steal, Nsteal)
        
        return dfs(0)