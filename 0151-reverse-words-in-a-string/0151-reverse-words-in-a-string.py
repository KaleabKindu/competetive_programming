class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        answer =[]
        for word in words:
            if word != '':
                answer.append(word)
        return " ".join(answer[::-1])