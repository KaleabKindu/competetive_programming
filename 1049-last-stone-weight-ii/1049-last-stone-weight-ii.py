class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        
        target = total // 2
        
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for stone in stones:
            for j in range(len(dp) - 1, stone - 1, -1):
                dp[j] |= dp[j - stone]
        
        answer = float('inf')
        
        for group_1 in range(len(dp)):
            if dp[group_1] == 1:
                group_2 = total - group_1
                answer = min(answer, abs(group_2 - group_1))
        return answer