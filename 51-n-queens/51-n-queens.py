class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        
        placement = [['.' for i in range(n)] for i in range(n)]
        
        cols = set()
        pdiagonals = set()
        ndiagonals = set()
        
        is_not_under_attack = lambda row, col: col not in cols and row - col not in \
                            pdiagonals and (row + col) not in ndiagonals
        
        def place_queen(row, col):
            placement[row][col] = 'Q'
            cols.add(col)
            pdiagonals.add(row - col)
            ndiagonals.add(row + col)
        def remove_queen(row, col):
            placement[row][col] = '.'
            cols.remove(col)
            pdiagonals.remove(row - col)
            ndiagonals.remove(row + col)    
        
        def backtrack(row = 0):
            if row >= n:
                answer.append(["".join(temp[:]) for temp in placement]) 
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    backtrack(row + 1)
                    remove_queen(row, col)
        
        backtrack()
        return answer