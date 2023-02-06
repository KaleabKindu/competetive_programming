class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=lambda x: len(x))
        dp = [1 for _ in range(n)]
        answer = 0
        for i in range(n - 1, -1, -1):
            temp = 0
            word1 = words[i]
            for j in range(i + 1, n):
                word2 = words[j]
                h, g = len(word1), len(word2)
                if g == h + 1:
                    out = 0
                    l, r = 0, 0
                    while l < h and r < g:
                        if word1[l] != word2[r]:
                            r += 1
                            out += 1
                        else:
                            l += 1
                            r += 1
                    if out == 1 or (l == h and r == g - 1):
                        temp = max(temp, dp[j])
            dp[i] += temp
            answer = max(answer, dp[i])
            
        return answer
                