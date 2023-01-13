from math import ceil
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        heap = []
        for num in nums:
            heappush(heap, -num)
        score = 0
        while k:
            node = -heappop(heap)
            score += node
            heappush(heap, -ceil(node/3))
            k -= 1
        
        return score
        
        