class Solution:
    def helper(self, nums):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] < nums[0]:
                end = mid - 1
            else:
                ans = mid
                start = mid + 1
        return ans
    def searchBinary(self,nums, left, right, target):
        start = left
        end = right
        while start <= end:
            mid=(start + end)//2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return -1
    def search(self, nums: List[int], target: int) -> int:
        index = self.helper(nums)
        left = self.searchBinary(nums, 0, index, target)
        right = self.searchBinary(nums, index + 1, len(nums) - 1, target)
        if left != -1:
            return left
        else:
            return right
        