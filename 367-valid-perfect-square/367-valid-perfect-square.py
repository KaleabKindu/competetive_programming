class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        start = 1
        end = num//2
        while start <= end:
            mid = (start + end)//2
            temp = mid * mid
            if temp < num:
                start = mid + 1
            elif temp > num:
                end = mid - 1
            else:
                return True
        return False
        