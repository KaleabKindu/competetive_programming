class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        visited = [False for i in range(len(nums))]
        path = []
        def bk():
            if len(path) == len(nums):
                answer.add(tuple(path[:]))
            
            for i in range(len(nums)):
                if not visited[i]:
                    path.append(nums[i])
                    visited[i] = True
                    bk()
                    visited[i] = False
                    path.pop()

        bk()
        return answer