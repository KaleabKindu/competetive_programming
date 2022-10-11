class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                if (len(stack) - 1) + n - i >= k:
                    stack.pop()
                else: break
            if len(stack) < k: stack.append(i)
            
        return [nums[i] for i in stack]