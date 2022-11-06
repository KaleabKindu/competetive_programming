class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        unique = deque(sorted(count.values()))
        
        while k > 0:
            if unique[0] <= k:
                least = unique.popleft()
                k -= least
            else:
                unique[0] -= k
                k = 0
                
        return len(unique)
                