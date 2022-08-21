class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isprime(n):
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        
        prime = 0
        for i in range(2, n + 1):
            if isprime(i):
                prime += 1
        
        return (factorial(prime) * factorial(n - prime) ) % (10**9 + 7)
            