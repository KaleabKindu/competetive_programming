class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = s.split(" ")
        reverse = []
        for word in sentence:
            reverse.append(word[::-1])
        return " ".join(reverse)