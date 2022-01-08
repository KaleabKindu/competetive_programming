class Solution:
    def reverseParentheses(self, s: str) -> str:
        stak=[]
        for i in s:
            if i != ')':
                stak.append(i)
            else:
                ans=[]
                while stak[-1]!='(':
                    ans.append(stak.pop())
                stak.pop()
                stak+=ans
        return "".join(stak)
