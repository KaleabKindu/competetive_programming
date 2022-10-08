class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        mindiff = float('inf')
        closest = 0           
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                total = nums[r] + nums[l] + nums[i]
                if abs(target - total) < mindiff:
                    closest = total
                    mindiff = abs(target - total)
                if total < target: 
                    l += 1
                elif total > target: 
                    r -= 1
                else:
                    l += 1
                    r -= 1
        return closest
            