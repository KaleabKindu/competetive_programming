class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        zeros = 0
        i = 0
        while i < n:
            if nums[i] == 0:
                j = i
                while j < n and nums[j] == 0:
                    j += 1
                temp = j - i
                zeros += (temp * (temp + 1))//2
                i = j
            else:
                i += 1
        return zeros