class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        dp = [1 for i in range(n)]
        answer = 1
        for i in range(n - 2, -1, -1):
            maxx = 0
            for j in range(i + 1, n):
                if pairs[i][1] < pairs[j][0]:
                    maxx = max(maxx, dp[j])
            dp[i] += maxx
            answer = max(dp[i], answer)
        
        return answer