class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(string):
            stack = []
            for char in string:
                if stack and stack[-1] == '(' and char == ')':
                    stack.pop()
                else:stack.append(char)
            return len(stack) == 0
        answer = []
        path = []
        def dp(cur = 0):
            if cur >= 2*n:
                if valid("".join(path)):
                    answer.append("".join(path))
                return 
            path.append('(')
            dp(cur + 1)
            path.pop()
            path.append(')')
            dp(cur + 1)
            path.pop()
        dp()
        return answer