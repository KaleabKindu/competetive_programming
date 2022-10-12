class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)        
        dp = defaultdict(lambda: defaultdict(int))
        answer = 0
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                diff = nums[j] - nums[i]
                dp[i][diff] = max(dp[i][diff], 1 + dp[j].get(diff, 1))
                answer = max(answer, dp[i][diff])
        return answer
                
                
                