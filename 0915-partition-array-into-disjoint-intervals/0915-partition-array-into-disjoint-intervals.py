class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        minimum = [num for num in nums]
        _min = nums[-1]
        for i in range(n - 2, -1, -1):
            _min = min(_min, nums[i])
            minimum[i] = _min
        maximum = float('-inf')
        for i in range(n):
            if i and minimum[i] >= maximum:
                return i
            maximum = max(maximum, nums[i])
        return 1
                
            