class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def capacity(mid):
            time = 0  
            for i in piles:
                time += ceil(i / mid)

            return h >= time
    
        
        left = 1
        right = max(piles)
        answer = 0
        while left <= right:
            mid = (left + right)//2
            
            if capacity(mid) :
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer