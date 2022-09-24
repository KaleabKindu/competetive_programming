class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # holds the numbers in each row
        rows = defaultdict(lambda: defaultdict(int))
        # holds the numbers in each column
        cols = defaultdict(lambda: defaultdict(int))
        # holds numbers in each 3x3 boxes
        boxes = defaultdict(lambda: defaultdict(int))
        candidates = [str(temp) for temp in range(1, 10)]
        # holds key value pair of an index to a the corresponding box
        box = {}
        
        # add the numbers to thier respective rows and cols
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    rows[i][board[i][j]] += 1
                    cols[j][board[i][j]] += 1
                    
        # add the numbers to their respective box           
        for  i in [0, 3, 6]:
            for m in [0, 3, 6]:
                for j in range(i, i + 3):
                    for k in range(m, m + 3):
                        box[(j, k)] = (i, m)
                        if board[j][k] != '.':
                            boxes[(i, m)][board[j][k]] += 1
                            
        is_valid = lambda i, j: rows[i][board[i][j]] <= 1  and cols[j][board[i][j]] <= 1 \
                    and boxes[box[(i, j)]][board[i][j]] <= 1 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not is_valid(i, j):
                    return False
        return True

