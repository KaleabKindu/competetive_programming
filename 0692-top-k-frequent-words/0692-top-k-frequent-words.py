class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        heap = []
        seen = set()
        for word in words:
            if word not in seen:
                heappush(heap, (-words.count(word), word))
                seen.add(word)
        
        return [temp[1] for temp in nsmallest(k, heap)]
            