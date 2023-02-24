class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        answer = 0
        i = 0
        while tickets[k]:
            if tickets[i]:
                tickets[i] -= 1
                answer += 1
            i = (i + 1)%n
        return answer