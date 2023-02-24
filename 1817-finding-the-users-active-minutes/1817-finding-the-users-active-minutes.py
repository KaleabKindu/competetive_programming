class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        n = len(logs)
        logs.sort()
        count = defaultdict(int)
        i = 0
        while i < n:
            j = i
            temp = set()
            while j < n and logs[i][0] == logs[j][0]:
                temp.add(logs[j][1])
                j += 1
            i = j
            count[len(temp)] += 1
        answer = []
        for i in range(k):
            answer.append(count[i + 1])
            
        return answer