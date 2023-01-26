class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        n = len(answers)
        
        rabbits = n
        
        count = Counter(answers)
        
        for key, val in count.items():
            if val < (key + 1):
                rabbits += key - val + 1
            elif key and val > (key + 1):
                temp = val % (key + 1)
                rabbits += key - temp + 1 if temp else 0
                
        return rabbits