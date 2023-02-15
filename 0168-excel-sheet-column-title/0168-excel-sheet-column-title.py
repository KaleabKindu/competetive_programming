class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = []
        while columnNumber > 0:
            answer.append(chr(65+(columnNumber-1)%26))
            columnNumber = (columnNumber-1) // 26
        answer.reverse()
        return ''.join(answer)
            