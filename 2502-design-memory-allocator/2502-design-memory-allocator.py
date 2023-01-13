class Allocator:

    def __init__(self, n: int):
        self.memory = [0 for _ in range(n)]
        self.mid = defaultdict(list)
        

    def allocate(self, size: int, mID: int) -> int:
        n = len(self.memory)
        i = 0
        while i < n:
            if not self.memory[i]:
                j = i
                while j < n and self.memory[j] == 0:
                    j += 1
                    if j - i == size:
                        self.memory[i] = size
                        self.mid[mID].append(i)
                        return i
                i = j
            else:
                i += self.memory[i]
                
        return -1
                
        

    def free(self, mID: int) -> int:
        units = 0
        for i in self.mid[mID]:
            units += self.memory[i]
            self.memory[i] = 0
        self.mid.pop(mID)
            
        return units
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)