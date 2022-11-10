class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        
        for h in range(12):
            hour = ""
            hour_bits = 0
            for bit in range(9):
                if h & (1 << bit) != 0:
                    hour_bits += 1
            if hour_bits <= turnedOn:
                hour += str(h) + ':'
                for m in range(60):
                    minute_bits = 0
                    for bit in range(7):
                        if m & (1 << bit) != 0:
                            minute_bits += 1
                    if minute_bits + hour_bits == turnedOn:
                        if m // 10 == 0:
                            answer.append(hour + '0' + str(m))
                        else:
                            answer.append(hour + str(m))
                        
        return answer
                        
                
            