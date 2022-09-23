class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        answer = float('inf')
        l, r = 0, n - 1
        while l <= r:
            mid  = (l + r)//2
            if nums[mid] >= nums[l]:
                answer = min(answer, nums[l])
                l = mid + 1
            elif nums[mid] < nums[r]:
                answer =min(answer, nums[mid])
                r = mid - 1
        return answer