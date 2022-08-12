class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:temp = str(x)
        else: temp = str(x)[1:]
        answer = temp[::-1]
        if x >= 0: answer = int(answer)
        elif x < 0: answer = -int(answer)
        
        
        if (2**31 - 1) >= answer >= -2**31: 
            return answer
        else: return 0
    
#     Time Complexity = O(n)
#     Space Complexity = O(n)
        