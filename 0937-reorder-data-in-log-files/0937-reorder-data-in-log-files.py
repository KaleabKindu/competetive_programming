class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digits = []
        letters = []
        for log in logs:
            temp = log.split(' ')
            if temp[1].isdigit():
                digits.append(" ".join(temp))
            else:
                letters.append(" ".join(temp))
        
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letters + digits