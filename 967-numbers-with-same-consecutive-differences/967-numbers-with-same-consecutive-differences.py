class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer = []
        path = []
        def dfs(num, path):
            if len(path) == n:
                return answer.append(int("".join(path)) )

            if (num + k) <= 9:
                path.append(str(num + k))
                dfs(num + k, path)
                path.pop()
            if 0 <= (num - k ) < num:
                path.append(str(num - k))
                dfs(num - k, path)
                path.pop()
        for i in range(1, 10):
            dfs(i, [str(i)])
        return answer
                