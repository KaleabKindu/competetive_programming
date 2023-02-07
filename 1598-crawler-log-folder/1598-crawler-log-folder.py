class Solution:
    def minOperations(self, logs: List[str]) -> int:
        n = len(logs)
        stack = 0
        for op in logs:
            if op[0] == '.' and op[1] == '.':
                if stack: stack -= 1
            elif op[0] != '.':
                stack += 1
        return stack
            