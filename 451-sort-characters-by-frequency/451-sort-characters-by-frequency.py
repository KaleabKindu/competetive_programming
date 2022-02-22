class Solution:
    def frequencySort(self, s: str) -> str:
        answer=''
        heap=[]
        frequency=Counter(s)
        for i,k in frequency.items():
            heapq.heappush(heap, (-k,i))
        while heap:
            letter=heapq.heappop(heap)
            answer+=letter[1]*-(letter[0])
        return answer
        