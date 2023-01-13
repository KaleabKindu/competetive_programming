class Solution:
    def maxJump(self, stones: List[int]) -> int:
        
        n = len(stones)
        
        maxjump = 0
        even = []
        odd = []
        for i in range(n):
            if not i or i % 2 == 0 or i == n - 1:
                even.append(stones[i])
            if not i or i % 2 != 0 or i == n - 1:
                odd.append(stones[i])
                
        for i in range(len(even) - 1):
            maxjump = max(maxjump, even[i + 1] - even[i])
            
        for i in range(len(odd) - 1):
            maxjump = max(maxjump, odd[i + 1] - odd[i])
        
        
        return maxjump
        