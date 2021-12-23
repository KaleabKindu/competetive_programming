class Solution:
    def oper(self,char,num1,num2):
        if char=='+':
            return int(num1)+int(num2)
        elif char=='-':
            return int(num2)-int(num1)
        elif char=='*':
            return int(num1)*int(num2)
        elif char=='/':
            return int(int(num2)/int(num1))
    def evalRPN(self, tokens: List[str]) -> int:
        operations=["+","-","*","/"]
        stack=[]
        for i in tokens:
            if i not in operations:
                stack.append(i)
            else:
                stack.append(self.oper(i,stack.pop(),stack.pop()))
        return stack[0]
