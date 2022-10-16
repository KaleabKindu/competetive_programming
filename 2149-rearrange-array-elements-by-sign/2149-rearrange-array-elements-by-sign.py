class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positive = []
        negative = []
        
        for i in range(n):
            if nums[i] < 0:
                negative.append(nums[i])
            elif nums[i] > 0:
                positive.append(nums[i])
        
        answer = []
        for i in range(n//2):
            answer.append(positive[i])
            answer.append(negative[i])
            
        return answer
                