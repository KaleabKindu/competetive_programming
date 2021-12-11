class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        myanswer=[]
        for i in range(1,n+1):
            if i % 3 ==0 and i % 5 ==0:
                myanswer.append('FizzBuzz')
            elif i % 3 ==0:
                myanswer.append('Fizz')
            elif i % 5 ==0:
                myanswer.append('Buzz')
            else:
                myanswer.append(str(i))
        return myanswer
