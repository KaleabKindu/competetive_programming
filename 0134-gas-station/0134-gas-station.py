class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        diff = []
        for i in range(n):
            diff.append(gas[i] - cost[i])
        
        answer = 0
        total = 0
        for i in range(n):
            total += diff[i]
            if total < 0:
                total = 0
                answer = i + 1
        
        return answer
        