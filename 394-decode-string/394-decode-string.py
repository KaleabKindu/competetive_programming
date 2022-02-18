class Solution:
    def decodeString(self, s: str) -> str:
        string=[]
        number=[]
        i=0
        res=''
        while i<len(s):
            if s[i].isdigit():
                temp=''
                while s[i].isdigit():
                    temp+=s[i]
                    i+=1
                number.append(int(temp))
            elif s[i]=='[':
                string.append(res)
                res=""
                i+=1
            elif s[i]==']':
                time=int(number.pop())
                temp=string.pop()
                temp+=res*time
                # for i in range(time):
                #     temp+=res
                res=temp
                i+=1
            else:
                res+=s[i]
                i+=1
        return res

        