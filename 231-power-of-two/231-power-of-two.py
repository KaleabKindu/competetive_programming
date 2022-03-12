class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        stack = [1]
        def powertwo():
            i = 1
            while stack[-1] < n:
                stack.append(2 * stack[-1])
            return True if stack[-1] == n else False
        
        return powertwo()