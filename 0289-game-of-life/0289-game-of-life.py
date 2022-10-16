class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        inbound = lambda i, j: 0 <= i < n and 0 <= j < m
        DIR = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        def neighbors(i, j):
            live_neighbor = 0
            for offset in DIR:
                r, c = i + offset[0], j + offset[1]
                if inbound(r, c):
                    if board[r][c] == 1 or board[r][c] == 2:
                        live_neighbor += 1
            return live_neighbor
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    live_neighbor = neighbors(i, j)
                    if live_neighbor < 2 or live_neighbor > 3:
                        board[i][j] = 2
                else:
                    live_neighbor = neighbors(i, j)
                    if live_neighbor == 3:
                        board[i][j] = 3
                        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 3:
                    board[i][j] = 1
                if board[i][j] == 2:
                    board[i][j] = 0
                
                
        
        