class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        answer = []
        in_bound = lambda i, j: 0 <= i < rows and 0 <= j <cols
        # starting row or col for each move
         
        # moves = [rStart, cStart + 1, rStart + 1, cStart - 1] # [right, down, left, up]
        moves = [cStart, rStart, cStart + 1, rStart + 1]
        while len(answer) < rows*cols:
            right, down, left, up = moves
            # move to the right
            for i in range(right, left + 1):
                if in_bound(down, i):
                    answer.append([down, i])
            right -= 1
            # move down
            for i in range(down + 1, up + 1):
                if in_bound(i, left):
                    answer.append([i, left])
            down -= 1
            # move left
            for i in range(left - 1, right - 1, -1):
                if in_bound(up, i):
                    answer.append([up, i])
            left += 1
            # move up
            for i in range(up - 1, down, -1):
                if in_bound(i, right):
                    answer.append([i, right])
            up += 1 
            moves = right, down, left, up 
        return answer