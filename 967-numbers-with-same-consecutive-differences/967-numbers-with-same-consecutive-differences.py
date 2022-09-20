class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer = []
        def dfs(digits, number):
            if digits == n:
                return answer.append(number)
            taildigit = number % 10
            if taildigit + k <= 9:
                dfs(digits + 1, (number * 10) + taildigit + k)
            if 0 <= (taildigit - k ) < taildigit:
                dfs(digits + 1, (number * 10) + taildigit - k)
        for i in range(1, 10):
            dfs(1, i)
        return answer
                