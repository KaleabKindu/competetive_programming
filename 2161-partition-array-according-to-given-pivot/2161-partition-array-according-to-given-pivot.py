class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        def helper(num):
            if num < pivot:
                return -1
            elif num > pivot:
                return 1
            return 0
        return sorted(nums, key=helper)
                
        