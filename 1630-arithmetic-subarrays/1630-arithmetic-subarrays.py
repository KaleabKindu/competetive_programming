class Solution:
    def check(self,l,r,nums):
        temp=nums[l:r+1]
        temp.sort()
        i=0
        while i < len(temp)-1:
            if temp[i+1]-temp[i] != temp[1]-temp[0]:
                return False
            i+=1
        return True
        
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer=[]
        i=0
        while i<len(l):
            answer.append(self.check(l[i],r[i],nums))
            i+=1
        return answer
            
        