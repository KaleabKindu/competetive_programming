class Solution:
    def isValid(self, s: str) -> bool:
        dict={'{':'}','(':')','[':']'}
        stack=[]
        for i in s:
            if i in dict.keys():
                stack.append(i)
            elif stack==[] or dict[stack.pop()]!= i:
                return False 
        if len(stack)==0:
            return True
        return False
        
