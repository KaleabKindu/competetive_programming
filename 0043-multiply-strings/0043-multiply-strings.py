class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        num_1 = 0
        for i in range(n):
            num_1 += int(num1[i]) * 10**(n - i - 1)
            
        num_2 = 0
        for i in range(m):
            num_2 += int(num2[i]) * 10**(m - i - 1)
        
        return str(num_1 * num_2)