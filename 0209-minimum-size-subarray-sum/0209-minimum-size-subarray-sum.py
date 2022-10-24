class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        n = len(nums)
        answer = float('inf')
        total = 0
        l, r = 0, 0
        while r < n:
            total += nums[r]
            while total >= target:
                answer = min(answer, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1
        
        return answer