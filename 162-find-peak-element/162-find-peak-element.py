class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if mid == 0 or nums[mid] > nums[mid - 1]:
                answer = mid
                start = mid + 1
            else:
                end = mid - 1
        return answer 