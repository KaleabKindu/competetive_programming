class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer = []
        def dfs(num, path):
            if path // (10 **(n - 1)) != 0:
                return answer.append(path)
            if (num + k) <= 9:
                dfs(num + k, (path * 10) + (num + k))
            if 0 <= (num - k ) < num:
                dfs(num - k, (path * 10) + (num - k))
        for i in range(1, 10):
            dfs(i, i)
        return answer
                