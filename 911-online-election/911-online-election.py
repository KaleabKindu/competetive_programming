class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.score={x:0 for x in persons}
        self.leadership = [self.persons[0]]
        self.score[self.persons[0]] += 1
        for i in range(1, len(persons)):
            self.score[self.persons[i]] += 1
            if self.score[self.persons[i]] > self.score[self.leadership[-1]]:
                self.leadership.append(persons[i])
            elif self.score[self.persons[i]] < self.score[self.leadership[-1]]:
                self.leadership.append(self.leadership[-1])
            else:
                self.leadership.append(self.persons[i])
    def q(self, t: int) -> int:
        start = 0
        end = len(self.leadership) - 1
        while start <= end:
            mid = (start + end)//2
            if self.times[mid] > t:
                end = mid - 1
            elif self.times[mid] < t:
                answer = mid
                start = mid + 1
            else:
                return self.leadership[mid]
        return self.leadership[answer]
        
         
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)