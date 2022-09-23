class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = dividend if dividend > 0 else -dividend
        b = divisor if divisor > 0 else -divisor
        answer = 0
        for i in range(32, -1,-1):
            if b << i <= a:
                a -= b << i
                answer += 1 << i
        answer = answer if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0 else -answer
        
        if answer < -2**31:
            return -2**31
        elif answer > (2**31) - 1:
            return (2**31) - 1
        return answer