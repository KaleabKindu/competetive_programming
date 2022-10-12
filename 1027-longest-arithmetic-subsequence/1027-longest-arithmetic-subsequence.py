class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)        
        dp = [[1] * 10001 for i in range(n) ]
        answer = 0
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                diff = nums[j] - nums[i]
                dp[i][diff - 500] = max(dp[i][diff - 500], 1 + dp[j][diff - 500])
                answer = max(answer, dp[i][diff - 500])
                
        return answer
                