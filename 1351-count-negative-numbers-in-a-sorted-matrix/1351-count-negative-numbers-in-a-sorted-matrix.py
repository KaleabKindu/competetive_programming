class Solution:
    def search(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] < 0:
            return right-left+1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < 0:
                right = mid - 1
            elif nums[mid] >= 0:
                left = mid + 1
        return (len(nums)-1) - right 
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            count += self.search(i)
        return count
        
        