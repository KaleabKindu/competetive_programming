class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        path = []
        def helper(i = 1, count = 0):
            if count == k:
                answer.append([*path])
                return 
            if i > n :
                return 
            helper(i + 1, count)
            path.append(i)
            helper(i + 1, count + 1)
            path.pop()
        helper()
        return answer