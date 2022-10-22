class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        answer = float('-inf')
        count = {'T': 0, 'F': 0 }
        l, r = 0, 0
        while r < n:
            if min(count['T'], count['F']) <= k:
                count[answerKey[r]] += 1
                r += 1
                if min(count['T'], count['F']) <= k: 
                    answer = max(answer, r - l)
            else:
                count[answerKey[l]] -= 1
                l += 1
        return answer