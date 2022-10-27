class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        if len(part) > len(s):
            return s
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if "".join(stack[-n:]) == part:
                for _ in range(n):
                    stack.pop()
            
        return "".join(stack)
                