class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        # starting row or col for each move
        moves = [0, m - 1, n - 1, 0] # [right, down, left, up]

        answer = []
        right, down, left, up = moves
        
        while right <= left and up <= down:
            right, down, left, up = moves
            # move to the right
            for i in range(right, down + 1):
                answer.append(matrix[right][i])
            right += 1
            
            # move down
            for i in range(right, left + 1):
                answer.append(matrix[i][down])
            down -= 1
            
            # move left
            for i in range(down, up - 1, -1):
                answer.append(matrix[left][i]) 
            left -= 1
            
            # move up
            for i in range(left, right - 1, -1):
                answer.append(matrix[i][up])
            up += 1
            moves = right, down, left, up 
            
        return answer[:n*m]
            