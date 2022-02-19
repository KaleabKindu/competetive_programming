class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==1:
            return "0"
        stak=[]
        for i in range(len(num)):
            while stak!=[] and stak[-1]  > num[i] and k>0:
                stak.pop()
                k-=1
            stak.append(num[i])
        stak=stak[:len(stak)-k]
        return str(int("".join(stak))) if "".join(stak) else "0"