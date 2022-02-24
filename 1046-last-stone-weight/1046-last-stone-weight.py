class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heappush(heap,-i)
        while len(heap) > 1:
            max1 = -heappop(heap)
            max2 = -heappop(heap)
            if max1 != max2:
                max1 = max1 - max2
                heappush(heap, -max1)
        return -heap[0] if heap else 0
        