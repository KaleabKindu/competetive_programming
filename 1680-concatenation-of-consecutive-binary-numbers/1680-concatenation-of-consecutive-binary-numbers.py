class Solution:
    def concatenatedBinary(self, n: int) -> int:
        number = []
        for i in range(1,n + 1):
            number.append(bin(i)[2:])
        number = "".join(number)
        return int(number, 2) % (10**9 + 7)