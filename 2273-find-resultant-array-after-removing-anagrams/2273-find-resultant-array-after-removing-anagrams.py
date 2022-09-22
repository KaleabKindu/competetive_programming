class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        answer = [words[0]]
        for i in range(n):
            if sorted(words[i]) != sorted(answer[-1]):
                answer.append(words[i])
        return answer