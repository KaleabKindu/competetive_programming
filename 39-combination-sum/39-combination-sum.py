class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        n = len(candidates)
        path = []
        def helper(i = 0, total = 0):
            if i >= n or total > target:
                return 
            if total == target:
                answer.append([*path])
                return 
            helper(i + 1, total)
            path.append(candidates[i])
            helper(i, total + candidates[i])
            path.pop()
        helper()
        return answer