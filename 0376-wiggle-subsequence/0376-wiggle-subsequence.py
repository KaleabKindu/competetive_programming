class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for i in range(n)]
        answer = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], 1 + dp[j][0])
                    answer = max(answer, dp[i][1])
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], 1 + dp[j][1])
                    answer = max(answer, dp[i][0])
        return answer
                
                
        
        
        
        
        
        
        
        
        
        
        
 