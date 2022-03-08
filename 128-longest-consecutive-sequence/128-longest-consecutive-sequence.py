class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number = set(nums)
        maxlength = 0
        length = 1
        
        for  num in nums:
            if num - 1 not in number:
                current = num
                while current + 1 in number:
                    current += 1
                    length += 1
                maxlength = max(length, maxlength)
                length = 1
        return maxlength