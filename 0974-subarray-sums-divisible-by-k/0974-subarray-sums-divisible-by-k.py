class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        modulo = defaultdict(int)
        modulo[0] = 1
        subarrays = 0
        prefix = 0
        for i in range(n):
            prefix += nums[i]
            subarrays += modulo[prefix % k]
            modulo[prefix % k] += 1
        return subarrays
                
                