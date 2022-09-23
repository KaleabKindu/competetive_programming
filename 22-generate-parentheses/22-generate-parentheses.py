class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(string):
            stack = 0
            for char in string:
                if char == ')':
                    stack -= 1
                else:stack += 1
                if stack < 0: return 0
            return stack == 0
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