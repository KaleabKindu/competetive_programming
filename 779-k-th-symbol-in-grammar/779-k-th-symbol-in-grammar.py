class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        parent=self.kthGrammar(n-1,math.ceil(k/2))
        isOdd=k%2!=0
        if parent==1:
            if isOdd:
                return 1
            return 0
        else:
            if isOdd:
                return 0
            return 1
            

            
        
        