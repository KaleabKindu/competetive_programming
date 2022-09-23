class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []
        seen = set()
        path = []
        def dfs(i = 0):
            if i == n:
                answer.append(list(path))
                return 
            for j in range(n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    path.append(nums[j])
                    dfs(i + 1)
                    seen.remove(nums[j])
                    path.pop()
        dfs()
        return answer
           
                