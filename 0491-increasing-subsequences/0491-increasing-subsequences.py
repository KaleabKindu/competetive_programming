class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        n = len(nums)
        path = []
        visited = [False for i in range(n)]
        def bk(num = float('-inf'), j = 0):
            if len(path) >= 2:
                answer.add(tuple(path[:]))
            for i in range(j, n):
                if nums[i] >= num and not visited[i]:
                    path.append(nums[i])
                    visited[i] = True
                    bk(nums[i], i + 1)
                    path.pop()
                    visited[i] = False
        bk()
        return answer