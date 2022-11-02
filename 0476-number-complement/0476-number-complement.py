class Solution:
    def findComplement(self, num: int) -> int:
        
        last_set_bit = 0
        for bit in range(33):
            if num & (1 << bit) != 0:
                last_set_bit = bit
        
        complement = 0
        for bit in range(last_set_bit):
            if num & (1 << bit) == 0:
                complement |= (1 << bit)
        
        return complement
            