class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()

        @cache
        def dp(passenger = 0):
            if passenger >= len(rides):
                return 0
            
            start, end, tip = rides[passenger]
            
            next_passenger = bisect_left(rides, end, lo = passenger + 1, key=lambda x:x[0])
            
            pickup_passenger = end - start + tip + dp(next_passenger)
            
            leave_passenger = dp(passenger + 1)
                
            return max(pickup_passenger, leave_passenger)
        
        return dp() 
        
