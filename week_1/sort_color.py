class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0,0,0]
        for i in nums:
            count[i]+=1
        index=0
        for i in range(3):
            for j in range(index,count[i]+index):
                nums[j]=i
            index+=count[i]
        
