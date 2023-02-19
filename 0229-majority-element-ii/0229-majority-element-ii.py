class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        answer = []
        i = 0
        while i < n:
            j = i
            while j < n and nums[i] == nums[j]:
                j += 1
            if j - i > n//3:
                answer.append(nums[i])
            i = j
            
        return answer
            