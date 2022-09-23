class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = set()
        n = len(candidates)
        path = []
        def helper(i = 0):
            if i >= n:
                return 
            if sum(path) >= target:
                if sum(path) == target:
                    answer.add(tuple([*path]))
                return 
            helper(i + 1)
            path.append(candidates[i])
            helper(i)
            path.pop()
        helper()
        return [list(temp) for temp in answer]