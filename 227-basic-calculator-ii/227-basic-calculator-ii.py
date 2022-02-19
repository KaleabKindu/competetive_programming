class Solution:
    def calculate(self, s: str) -> int:
        lis=s.split(" ")
        s="".join(lis)
        operand=[]
        operator=[]
        i=0
        while i < len(s):
            if s[i].isdigit():
                temp=""
                while i<len(s) and s[i].isdigit():
                    temp+=s[i]
                    i+=1
                if operand==[]:
                    operand.append(int(temp))
                elif operator[-1]=='*':
                    operator.pop()
                    operand.append(operand.pop()*int(temp))
                elif operator[-1]=='/':
                    operator.pop()
                    operand.append(operand.pop()//int(temp))   
                else:
                    operand.append(int(temp)) 
                continue
            else:
                operator.append(s[i])
                i+=1
        i=numm=0
        summ=0
        while i<len(operator):
            if i==0:
                if operator[i]=='+':
                    summ+=operand[numm] + operand[numm+1]
                else:
                    summ+=operand[numm] - operand[numm+1]  
                numm+=2
            elif operator[i]=='+':
                summ+=operand[numm]
                numm+=1
            elif operator[i]=='-':
                summ-=operand[numm]
                numm+=1
            i+=1
        return operand[0] if not operator else summ

                
        
        
        
        
        
        

            
            