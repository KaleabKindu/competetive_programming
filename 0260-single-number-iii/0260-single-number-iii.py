class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []
        nums.sort()
        i = 0
        while i < n:
            count = 1
            j = i + 1
            while j < n and nums[i] == nums[j]:
                count += 1
                j += 1
            if count == 1:
                answer.append(nums[i])
            i = j
            
        return answer