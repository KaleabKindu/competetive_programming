class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        temp = list(zip(growTime, plantTime))
        
        temp.sort(reverse=True)
        answer = 0
        days = 0
        for grow, plant in temp:
            days += plant
            answer = max(answer, days + grow)
        return answer