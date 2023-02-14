class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        prefix = []
        suffix = deque()
        acc = 0
        for i in range(n):
            if s[i] == 'b':
                acc += 1
            prefix.append(acc)
        acc = 0
        for i in range(n - 1, -1, -1):
            if s[i] == 'a':
                acc += 1
            suffix.appendleft(acc)
            
        answer = min(prefix[n - 1], suffix[0])
        for i in range(n - 1):
            answer = min(answer, prefix[i] + suffix[i + 1])
            
        return answer
            