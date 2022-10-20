class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        answer = float('-inf')
        total = 0
        l, r = 0, 0
        while r < n:
            total += nums[r]
            while total + k < nums[l] * (r - l + 1):
                total -= nums[l]
                l += 1
            answer = max(answer, r - l + 1)
            r += 1

        return answer
                
            