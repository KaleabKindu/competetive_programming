class Solution:
    def smallestSubsequence(self, s: str) -> str:
        unique = len(set(s))
        stack = []
        right_most_index = {}
        for i in range(len(s)):
            right_most_index[s[i]] = i
        n = len(s)
        seen = set()
        for i in range(n):
            char = s[i]
            if char in seen:
                continue
            while stack and stack[-1] > char and right_most_index[stack[-1]] > i:
                seen.remove(stack.pop())
                
            if len(stack) < unique:
                seen.add(char)
                stack.append(char)
                
        return "".join(stack)
                