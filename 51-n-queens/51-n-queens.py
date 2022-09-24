class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        
        placement = ['.' for i in range(n)]
        path = []
        
        cols = set()
        pdiagonals = set()
        ndiagonals = set()
        
        is_not_under_attack = lambda row, col: col not in cols and row - col not in \
                            pdiagonals and (row + col) not in ndiagonals
        
        def place_queen(row, col):
            placement[col] = 'Q'
            path.append("".join(placement[:]))
            placement[col] = '.'
            cols.add(col)
            pdiagonals.add(row - col)
            ndiagonals.add(row + col)
        def remove_queen(row, col):
            path.pop()
            cols.remove(col)
            pdiagonals.remove(row - col)
            ndiagonals.remove(row + col)    
        
        def backtrack(row = 0):
            if row >= n:
                answer.append([*path]) 
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    backtrack(row + 1)
                    remove_queen(row, col)
        
        backtrack()
        return answer