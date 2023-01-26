class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for sc, des, price in flights:
            graph[sc].append((price, des))
        
        best = defaultdict(lambda: defaultdict(lambda: float('inf')))
        
        heap = [(0, src, 0)]
        
        heapify(heap)
        
        while heap:
            weight, node, steps = heappop(heap)
            if node == dst:
                return weight
            if steps == k + 1:
                continue
            for price, child in graph[node]:
                new_price = weight + price
                if new_price < best[child][steps + 1]:
                    best[child][steps + 1] = new_price
                    heappush(heap,(new_price, child, steps + 1))
                    
        return -1
        
        