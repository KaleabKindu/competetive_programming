class Solution:
    def firstbinary(self,nums,target):
        left=0
        right=len(nums)-1
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if target < nums[mid]:
                right=mid-1
            elif target > nums[mid]:
                left=mid+1
            else:
                ans=mid
                right=mid-1
        return ans
    def secondbinary(self,nums,target):
        left=0
        right=len(nums)-1
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if target < nums[mid]:
                right=mid-1
            elif target > nums[mid]:
                left=mid+1
            else:
                ans=mid
                left=mid+1
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lindex=self.firstbinary(nums,target)
        rindex=self.secondbinary(nums,target)
        return [lindex,rindex]
        
        
        
        
        
        # left=0
        # right=len(nums)-1
        # while left<=right:
        #     mid=(left+right)//2
        #     if target < nums[mid]:
        #         right=mid-1
        #     elif target > nums[mid]:
        #         left=mid+1
        #     else:
        #         lindex=self.binary(nums,target,left,mid-1)
        #         rindex=self.binary(nums,target,mid+1,right)
        #         if lindex==-1:
        #             lindex=mid
        #         elif rindex==-1:
        #             rindex==mid
        #         else:
        #             return [lindex,rindex]
        # return [-1,-1]
