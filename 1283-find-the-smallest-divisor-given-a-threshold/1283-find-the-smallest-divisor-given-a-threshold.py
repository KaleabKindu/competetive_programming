class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def helper(divisor):
            summ = 0
            for i in nums:
                summ += math.ceil(i/divisor)
            return summ
        left = 1
        right = max(nums)
        while left <= right:
            mid=(left + right)//2
            if helper(mid) > threshold:
                left = mid + 1
            elif helper(mid) < threshold:
                # print(helper(mid), mid)
                answer = mid
                right = mid - 1
            else:
                # print(helper(mid), mid)
                answer = mid
                right = mid - 1
        return  answer
            
            
        