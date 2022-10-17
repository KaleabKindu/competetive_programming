class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        n = len(intervals)
        answer = []
        i = 0
        while i < n:
            start, end = intervals[i]
            j = i + 1
            while j < n and  end >= intervals[j][0] and start <= intervals[j][1]:
                start = min(start, intervals[j][0])
                end = max(end, intervals[j][1])
                j += 1
            
            answer.append([start, end])
            i = j
            
        return answer