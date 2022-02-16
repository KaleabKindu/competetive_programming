class Solution:
    def compress(self, chars: List[str]) -> int:
        s=[]
        cur=0
        while cur<len(chars):
            s.append(chars[cur])
            nex=cur+1
            count=1
            while nex<len(chars) and chars[cur]==chars[nex]:
                count+=1
                nex+=1
            if count!=1:
                if count>=10:
                    for i in str(count):
                        s.append(i)
                else:
                    s.append(str(count))
            cur=nex
        for i in range(len(s)):
            chars[i]=s[i]

        return len(s)
                