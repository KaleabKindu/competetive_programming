class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                heappush(heap, -((nums[i]-1) * (nums[j]-1)))
        return -heap[0]