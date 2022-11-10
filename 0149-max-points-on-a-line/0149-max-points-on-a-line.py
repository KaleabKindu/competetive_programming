class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def dfs(i, slope):
            if i == n:
                return 0
            res = 0
            for j in range(i + 1, n):
                _slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) if (points[j][0] - points[i][0]) else float('inf')
                if slope == _slope:
                    res = max(res, 1 + dfs(j, slope))
            return res
        answer = 1
        for i in range(n):
            for j in range(i + 1, n):
                slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) if (points[j][0] - points[i][0]) else float('inf')
                answer = max(answer, 2 + dfs(j, slope))
        return answer