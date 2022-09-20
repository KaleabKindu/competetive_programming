class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            temp = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    temp = max(temp, 1 + dp(j))
            return temp
        answer = 0
        for i in range(n):
            answer = max(dp(i), answer)
        return answer