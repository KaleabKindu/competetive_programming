class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = -1
        off = 0
        while True:
            temp = float('inf')
            summ = 0
            for i in range(n):
                if nums[i] > 0:
                    nums[i] -= off
                    if nums[i] > 0:
                        temp = min(temp, nums[i])
                summ += nums[i]
            off = temp
            operations += 1
            if not summ:
                break
        return operations
            