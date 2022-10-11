class Solution:
    def smallestSubsequence(self, s: str) -> str:
        unique = len(set(s))
        stack = []
        n = len(s)
        for i in range(n):
            char = s[i]
            if char in stack:
                continue
            while stack and stack[-1] > char and stack[-1] in s[i:]:
                stack.pop()
            if len(stack) < unique:
                stack.append(char)
                
        return "".join(stack)
                