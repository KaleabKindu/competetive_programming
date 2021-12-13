class Solution:
    def sortSentence(self, s: str) -> str:
        lst=s.split(" ")
        sorted=['' for _ in lst]
        for word in lst:
            sorted[int(word[-1])-1]=word[:-1]
        return " ".join(sorted)
