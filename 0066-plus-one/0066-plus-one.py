class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        number = 0
        
        for i in range(n):
            number += digits[i] * 10**(n - i - 1)
        
        return list(str(number + 1))