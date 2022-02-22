class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency={}
        for i in words:
            frequency[i]=frequency.get(i,0)+1
        frequency=sorted(frequency.items())
        frequency=dict(frequency)
        return heapq.nlargest(k,frequency.keys(),frequency.get)