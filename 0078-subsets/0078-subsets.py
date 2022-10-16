class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = set()
        path = []
        def bk(i = 0):
            if i >= n:
                answer.add(tuple(path))
                return
            answer.add(tuple(path))
            bk(i + 1)
            path.append(nums[i])
            bk(i + 1)
            path.pop()
        bk()
        return answer