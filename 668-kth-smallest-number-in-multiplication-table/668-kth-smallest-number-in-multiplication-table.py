class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def helper(trialCount):
            count = 0
            for i in range(1, m+1):
                count += min(trialCount // i, n)
            return count
        start = 1
        end = m * n
        while start < end:
            mid =  (start + end)//2
            count = helper(mid)
            if count < k:
                start = mid + 1
            else:
                end = mid
        return end
            
        