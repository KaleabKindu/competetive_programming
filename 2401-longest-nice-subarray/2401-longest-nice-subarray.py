class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        nice = 0
        l, r = 0, 0
        while r < n:
            if nice & nums[r] == 0:
                nice |= nums[r]
                r += 1 
                answer = max(answer, r - l)
            else:
                nice ^= nums[l]
                l += 1
        
        return answer
            