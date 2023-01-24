class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        answer = []
        for char in order:
            answer.append(char * count[char])
            if char in count:
                count.pop(char)
        
        for char in  count:
            answer.append(char*count[char])
        
        return "".join(answer)