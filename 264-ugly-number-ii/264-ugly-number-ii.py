class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap=[1]
        visited=set([1])
        generators=[2,3,5]
        j=0
        while j<n:
            current=heappop(heap)
            for i in generators:
                if current*i not in visited:
                    heappush(heap,current*i)
                    visited.add(current*i)
            j+=1
        return current
        