class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = {} 
        heap = []
        for i in score:
            heappush(heap, -i)
        if heap:
            temp[-heappop(heap)] = "Gold Medal"
        if heap:
            temp[-heappop(heap)] = "Silver Medal"
        if heap:
            temp[-heappop(heap)] = "Bronze Medal"
        while heap:
            tmp = len(temp) + 1
            temp[-heappop(heap)] = str(tmp)
        answer = []
        for i in score:
            answer.append(temp[i])
        return answer
        
        
        
        
        
        