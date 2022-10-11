class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        unique = len(set(s))
        n = len(s)
        rightindex = {}
        for i in range(n):
            rightindex[s[i]] = i
        seen = set()
        for i in range(n):
            char = s[i]
            if char in seen:
                continue
            while stack and stack[-1] > char and rightindex[stack[-1]] > i:
                seen.remove(stack.pop())
            if len(stack) < unique:
                seen.add(char)
                stack.append(char)
        return "".join(stack)