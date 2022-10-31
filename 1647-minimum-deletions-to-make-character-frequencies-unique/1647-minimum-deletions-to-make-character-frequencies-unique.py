class Solution:
    def minDeletions(self, s: str) -> int:
        characters = Counter(s)
        frequency = sorted(characters.values(), reverse=True)
        delete = 0
        for i in range(1, len(frequency)):
            if frequency[i] == frequency[i - 1]:
                frequency[i] -= 1
                delete += 1
            elif frequency[i] > frequency[i - 1]:
                val = frequency[i - 1] - 1 if frequency[i - 1] else 0
                remove = frequency[i] - val
                frequency[i] = val
                delete += remove
            
        return delete
            