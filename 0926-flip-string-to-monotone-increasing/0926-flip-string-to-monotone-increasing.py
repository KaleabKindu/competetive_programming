class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        suffix = deque()
        acc = 0
        for i in range(n - 1, -1, -1):
            acc += 1 - int(s[i])
            suffix.appendleft(acc)
            
        one = 0
        flips = float('inf')
        for i in range(n):
            flips = min(flips, one + suffix[i])
            one += int(s[i])
        
        prefix = []
        acc = 0
        for i in range(n):
            acc += int(s[i])
            prefix.append(acc)
            
        zero = 0
        for i in range(n - 1, -1, -1):
            flips = min(flips, zero + prefix[i])
            zero += 1 - int(s[i])
                       
        return flips
            
            
        
        