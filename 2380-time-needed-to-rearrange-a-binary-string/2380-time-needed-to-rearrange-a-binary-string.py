class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n = len(s)
        s = list(s)
        answer = 0
        
        while True:
            i = 0
            found = False
            while i < n - 1:
                if s[i] == '0' and s[i + 1] == '1':
                    s[i] = '1'
                    s[i + 1] = '0'
                    i += 2
                    found = True
                else:
                    i += 1
            if not found:
                break
            answer += 1
            
        return answer