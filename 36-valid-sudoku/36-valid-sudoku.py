class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # holds the numbers in each row
        rows = defaultdict(set)
        # holds the numbers in each column
        cols = defaultdict(set)
        # holds numbers in each 3x3 boxes
        boxes = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in rows[i] and board[i][j] not in cols[j] and board[i][j] not in boxes[(i//3, j//3)]:
                        rows[i].add(board[i][j])
                        cols[j].add(board[i][j])
                        boxes[(i//3, j//3)].add(board[i][j])
                    else: return False
        
        return True

