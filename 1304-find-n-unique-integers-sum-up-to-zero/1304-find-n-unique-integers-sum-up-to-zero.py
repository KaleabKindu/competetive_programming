class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = [0 for _ in range(n)]
        
        i, j = 0, n - 1
        while i <= j:
            if i == j:
                answer[i] = 0
                break
            answer[i] = i + 1
            answer[j] = -i - 1
            i += 1
            j -= 1
        return answer