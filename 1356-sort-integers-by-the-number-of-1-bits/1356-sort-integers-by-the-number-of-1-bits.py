class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ones = [0] * n
        
        for i in range(n):
            ones[i] = bin(arr[i])[2:].count('1')
            
        answer = []
        for index, val in enumerate(ones):
            answer.append((val, arr[index]))
        return [temp[1] for temp in sorted(answer)]