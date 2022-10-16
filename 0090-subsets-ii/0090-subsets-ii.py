class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        answer = set()
        for mask in range(2**n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            answer.add(tuple(subset))
            
        return answer