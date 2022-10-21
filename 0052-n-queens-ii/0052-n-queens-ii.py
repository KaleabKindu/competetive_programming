class Solution:
    def totalNQueens(self, n: int) -> int:
        
        self.answer = 0
        
        cols = set()
        
        pdiagonal = set()
        
        ndiagonal = set()
        
        is_not_under_attack = lambda r, c: c not in cols and r - c not in pdiagonal and r + c not in ndiagonal
        
        def place_queen(row, col):
            cols.add(col)
            pdiagonal.add(row - col)
            ndiagonal.add(row + col)
        def remove_queen(row, col):
            cols.remove(col)
            pdiagonal.remove(row - col)
            ndiagonal.remove(row + col)    
        
        
        def backtrack(row = 0):
            if row >= n:
                self.answer += 1
                return 
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row,col)
                    backtrack(row + 1)
                    remove_queen(row, col)
                    
        backtrack()
        return self.answer
                    
        
        