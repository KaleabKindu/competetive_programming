class Solution:     
    def hIndex(self, citations: List[int]) -> int:
        hindex = start = 0
        end = citations[-1]
        while start <= end:
            mid = (start + end)//2
            index = bisect_left(citations, mid) 
            if (len(citations) - index) >= mid:
                answer = mid
                start = mid + 1
            else:
                end = mid - 1
        return answer
                

            
            
        