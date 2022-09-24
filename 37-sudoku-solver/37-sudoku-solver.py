class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # holds the numbers in each row
        rows = defaultdict(set)
        # holds the numbers in each column
        cols = defaultdict(set)
        # holds numbers in each 3x3 boxes
        boxes = defaultdict(set)
        candidates = [str(temp) for temp in range(1, 10)]
        # holds key value pair of an index to a the corresponding box
        box = {}
        
        # add the numbers to thier respective rows and cols
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    
        # add the numbers to their respective box           
        for  i in [0, 3, 6]:
            for m in [0, 3, 6]:
                for j in range(i, i + 3):
                    for k in range(m, m + 3):
                        box[(j, k)] = (i, m)
                        if board[j][k] != '.':
                            boxes[(i, m)].add(board[j][k])
                            
        is_valid = lambda i, j, val: val not in rows[i] and val not in cols[j] and val not \
                            in boxes[box[(i, j)]]      
        def place_number(row, col, candidate):
            rows[row].add(candidate)
            cols[col].add(candidate)
            boxes[box[(row, col)]].add(candidate)
            board[row][col] = candidate
        def remove_number(row, col, candidate):
            rows[row].remove(candidate)
            cols[col].remove(candidate)
            boxes[box[(row, col)]].remove(candidate)
            board[row][col] = '.'    
        n = len(board)
        def backtrack():
            for i in range(n):
                for j in range(n):
                    if board[i][j] == '.':
                        for candidate in candidates:
                            if is_valid(i, j, candidate):
                                place_number(i, j, candidate)
                                if backtrack(): return True
                                remove_number(i, j, candidate)
                        return False
                    
            # returns true only if no '.' character remains
            return True

        backtrack()
