class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        l, r = 0, 0
        increasing = deque()
        decreasing = deque()
        length = float('-inf')
        while r < n:  
            # add the new element to the increasing queue
            while increasing and increasing[-1][1] > nums[r]:
                    increasing.pop()
            increasing.append((r,nums[r]))
            
            # add the new element to the increasing queue
            while decreasing and decreasing[-1][1] < nums[r]:
                decreasing.pop()
            decreasing.append((r,nums[r]))
            
            #get the minimum number of the current window
            while increasing and not l <= increasing[0][0] <= r:
                increasing.popleft()
            curmin = increasing[0][1]
            
            #get the maximum number of the current window
            while decreasing and not l <= decreasing[0][0] <= r:
                decreasing.popleft()
            curmax = decreasing[0][1]

            if curmax - curmin <= limit:
                r += 1  
                length = max(length, r - l)
            else:
                l += 1
                r += 1
        return length
    
    
   
            
            
            