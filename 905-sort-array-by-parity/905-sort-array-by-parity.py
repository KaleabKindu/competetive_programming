class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = set()
        
        answer = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.add(i)
        
        for index in even:
            answer.append(nums[index])
        
        for i in range(len(nums)):
            if i not in even:
                answer.append(nums[i])
                
        return answer
        
        
        