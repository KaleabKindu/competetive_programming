class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        answer = [[0] * n for i in range(n)]
        
        # starting row or col for each move
        moves = [0,   n - 1, n - 1, 0] # [right, down, left, up]

        num = 1
        
        while num <= n**2:
            right, down, left, up = moves
            # move to the right
            for i in range(right, down + 1):
                answer[right][i] = num
                num += 1
            right += 1
            
            # move down
            for i in range(right, left + 1):
                answer[i][down] = num
                num += 1
            down -= 1
            
            # move left
            for i in range(down, up - 1, -1):
                answer[left][i] = num
                num += 1
            left -= 1
            
            # move up
            for i in range(left, right - 1, -1):
                answer[i][up] = num
                num += 1
            up += 1
            moves = right, down, left, up 
            
        return answer
            
            
            
           
            
            
            
        