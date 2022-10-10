class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        answer = float('-inf')
        
        path = set()
        @cache
        def dfs(i = 0):
            path.add(i)
            if nums[i] not in path:
                dfs(nums[i])
        for i in range(n):
            dfs(i)
            answer = max(answer, len(path))
            path.clear()
        return answer
        
            