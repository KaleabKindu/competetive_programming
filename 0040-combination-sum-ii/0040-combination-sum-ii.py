class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        n = len(candidates)
        count = Counter(candidates)
        answer = set()
        path = []
        def bk(total = 0):
            if total >= target:
                if total == target:
                    answer.add(tuple(sorted(path)))
                return
            temp = list(count.keys())
            for key in temp:
                count[key] -= 1
                if count[key] == 0:
                    count.pop(key)
                path.append(key)
                bk(total + key)
                path.pop()
                count[key] += 1
        bk()
        return answer