class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True for i in range(n)]
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i + i, n , i):
                    is_prime[j] = False
                
        return is_prime.count(True)
                