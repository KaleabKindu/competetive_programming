class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []
        seen = set([_ for _ in nums])
        path = []
        def dfs(i = 0):
            if i == n:
                answer.append([*path])
                return 
            for num in list(seen):
                seen.remove(num)
                path.append(num)
                dfs(i + 1)
                seen.add(num)
                path.pop()
        dfs()
        return answer
           
                