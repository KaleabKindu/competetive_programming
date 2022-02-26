class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x
        while start <= end:
            mid = (start + end)//2
            if mid * mid < x:
                start = mid + 1
            elif mid * mid > x:
                end = mid - 1
            else:
                return mid
        return end