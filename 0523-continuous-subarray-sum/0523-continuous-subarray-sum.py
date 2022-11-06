class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        modulo = defaultdict(int)
        modulo[0] = -1
        prefix = 0
        for i in range(n):
            prefix += nums[i]
            if prefix % k in modulo:
                if i - modulo[prefix % k] >= 2:
                    return True
            else:
                modulo[prefix % k] = i
        return False