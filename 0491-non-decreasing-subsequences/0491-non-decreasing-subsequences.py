class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        n = len(nums)
        path = []
        visited = [False for i in range(n)]
        def bk(i, prev):
            if len(path) > 1:
                answer.add(tuple(path))
            for j in range(i + 1, n):
                if prev <= nums[j]:
                    path.append(nums[j])
                    bk(j, nums[j])
                    path.pop()
        
        
        for i in range(n):
            path.append(nums[i])
            bk(i, nums[i])
            path.pop()
            
        return answer