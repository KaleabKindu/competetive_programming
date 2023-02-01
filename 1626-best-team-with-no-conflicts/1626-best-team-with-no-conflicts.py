class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        
        temp = list(zip(ages, scores))
        
        temp.sort()
        
        dp = [score for age, score in temp]
        answer = 0
        for i in range(n - 1, -1, -1):
            score = 0
            for j in range(i + 1, n):
                if temp[i][1] <= temp[j][1]:
                    score = max(score, dp[j])
            dp[i] += score
            answer = max(answer, dp[i])
            
        return answer
                