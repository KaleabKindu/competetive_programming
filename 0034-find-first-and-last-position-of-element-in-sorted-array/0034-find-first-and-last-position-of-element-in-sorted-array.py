class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        left = -1
        right = -1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                left = mid
                r = mid - 1
                
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                right = mid
                l = mid + 1
        return [left, right]
                