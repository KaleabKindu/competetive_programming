class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        hindex = 0
        for i in range(len(citations) - 1, -1, -1):
            count = len(citations) - i
            if citations[i] >= count:
                hindex += 1
            else:
                break
        return hindex
            
            
        