class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        for i in range(n):
            while stack and stack[-1] > nums[i] and (len(stack) - 1) + n - i >= k:
                stack.pop()
            if len(stack) < k: 
                stack.append(nums[i])
                
        return stack