class Solution:
    @lru_cache()
    def fib(self, n: int) -> int:
        if n <= 1:
            return 0 if n == 0 else 1
        else:
            return self.fib(n - 2) + self.fib(n - 1)
        