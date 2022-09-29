class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        n = len(arr)
        for i in range(n):
            heappush(heap, (abs(arr[i] - x), arr[i]))
        answer = []
        i = 0
        while i < k:
            answer.append(heappop(heap)[1])
            i += 1
        answer.sort()
        return answer
        