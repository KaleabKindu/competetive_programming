class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        letters = list(s)
            
        answer = []
        path = []
        def backtrack(i = 0):
            if i == n:
                answer.append("".join(path))
                return
            if letters[i].isdigit():
                path.append(letters[i])
                backtrack(i + 1)
                path.pop()
            else:    
                # change to lowercase
                letters[i] = chr(ord(letters[i]) | ord(' '))
                path.append(letters[i])
                backtrack(i + 1)
                path.pop()

                # change to uppercase
                letters[i] = chr(ord(letters[i]) & ord('_'))
                path.append(letters[i])
                backtrack(i + 1)
                path.pop()
            
        backtrack()
        
        return answer
        
            