import math
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return  0
        n = len(nums)
        def reverse_number(num):
            rev_num = 0
            while num:
                digit = num % 10
                num = num // 10
                rev_num = rev_num*10 + digit
            return rev_num
        
        unique = defaultdict(int)
        for i in range(n):
            reverse = reverse_number(nums[i])
            unique[nums[i] - reverse] += 1
            
        nice = 0
        for val in unique.values():
            nice += (val * (val - 1) // 2)
            
        return nice % (10**9 + 7)