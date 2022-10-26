class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        nums = [1,1]
        prev = 1
        cur = 1
        while cur + prev <= k:
            _next = cur + prev
            nums.append(_next)
            prev = cur
            cur = _next
        answer = 0
        while k > 0:
            num = nums.pop()
            if num <= k:
                answer += 1
                k -= num
        return answer