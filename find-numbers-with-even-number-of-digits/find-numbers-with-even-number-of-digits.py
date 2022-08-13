class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        length, string = len, str
        evencount = 0
        for num in nums:
            if length(string(num)) % 2 == 0:
                evencount += 1
        return evencount