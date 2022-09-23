class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        answer = []
        path = []
        letters = {
            '2':['a','b','c'], '3':['d','e','f'],'4':['g','h','i'],
            '5':['j','k','l'], '6':['m','n','o'],'7':['p','q','r','s'],
            '8':['t','u','v'], '9':['w','x','y','z'],
        }
        def helper(i = 0):
            if i >= n:
                if path:
                    answer.append("".join(path))
                return 
            for letter in letters[digits[i]]:
                path.append(letter)
                helper(i + 1)
                path.pop()
        helper()
        return answer
        
            