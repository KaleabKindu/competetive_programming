class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        characters = defaultdict(int)
        def valid(word):
            chars = set()
            for char in word:
                chars.add(char)
                if characters[char] > 0:
                    return False
            return True and len(chars) == len(word)
        
        self.answer = 0
        def bk(i = 0, length = 0):
            self.answer = max(self.answer, length)
            for j in range(i, n):
                if valid(arr[j]):
                    for char in arr[j]:
                        characters[char] += 1
                    bk(j + 1, length + len(arr[j]))
                    for char in arr[j]:
                        characters[char] -= 1
        
        bk()
        return self.answer
                    
                    
                