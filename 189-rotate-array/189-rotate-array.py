class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        start,end=0,len(nums)-1
        while start < end:
            nums[start],nums[end]=nums[end],nums[start]
            start,end=start+1,end-1
            
            
        start,end=0,k-1
        while start < end:
            nums[start],nums[end]=nums[end],nums[start]
            start,end=start+1,end-1
            
        start,end=k,len(nums)-1
        while start < end:
            nums[start],nums[end]=nums[end],nums[start]
            start,end=start+1,end-1
            
            
        
                
            
        
        