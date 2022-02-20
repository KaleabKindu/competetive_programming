class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxArea=0
        while left<right:
            Area=(right-left)*min(height[left],height[right])
            maxArea=max(maxArea,Area)
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
                
        return maxArea
            
        
        
        