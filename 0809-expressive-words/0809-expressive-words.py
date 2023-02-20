class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        n = len(s)
        answer = 0
        for word in words:
            m = len(word)
            i = 0
            j = 0
            pos = True
            while i < n:
                if j >= m or word[j] != s[i]:
                    pos = False
                    break
                k = i
                while k < n and s[i] == s[k]:
                    k += 1
                temp = k - i
                i = k
                k = j
                while k < m and word[j] == word[k]:
                    k += 1
                if k - j != temp and( temp < 3 or temp < k - j):
                    pos = False
                    break
                j = k
                
            if n >= m  and j == m and pos:
                answer += 1
        return answer