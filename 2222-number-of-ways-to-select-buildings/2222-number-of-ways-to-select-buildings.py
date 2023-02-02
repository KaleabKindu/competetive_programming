class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        
        zerol, zeror = 0, s.count('0')
        onel, oner = 0, n - zeror
        
        answer = 0
        for i in range(n):
            if s[i] == '0':
                answer += onel * oner
                zerol += 1
                zeror -= 1
            else:
                answer += zerol * zeror
                onel += 1
                oner -= 1
                
        return answer