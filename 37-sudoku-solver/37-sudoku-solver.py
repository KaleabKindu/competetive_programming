class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        candidates = [str(temp) for temp in range(1, 10)]
        box = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    
        for  i in [0, 3, 6]:
            for m in [0, 3, 6]:
                for j in range(i, i + 3):
                    for k in range(m, m + 3):
                        box[(j, k)] = (i, m)
                        if board[j][k] != '.':
                            boxes[(i, m)].add(board[j][k])
                            
        # print(box)
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
            return True

        backtrack()
