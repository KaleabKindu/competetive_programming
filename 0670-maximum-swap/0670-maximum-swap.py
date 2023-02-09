class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, list(str(num))))
        for i in range(len(num)-1):
            index = i
            for j in range(i+1, len(num)):
                if num[j] >= num[index]:
                    index = j
            if i != index and num[i] != num[index]:
                num[i], num[index] = num[index], num[i]
                break
        
        return int("".join(map(str, num)))
            