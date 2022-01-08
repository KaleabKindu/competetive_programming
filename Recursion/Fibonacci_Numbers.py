class Solution:
    def fib(self, n: int) -> int:
        dic={}
        if n<=1:
            return n
        else:
            if n in dic:
                return dic[n]
            else:
                dic[n]=self.fib(n-2)+self.fib(n-1)
                return dic[n]
