class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        inbound = lambda i, j: 0 <= i < n and 0 <= j < m
        DIR = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        dies = set()
        lives = set()
        def neighbors(i, j):
            live_neighbor = 0
            for offset in DIR:
                r, c = i + offset[0], j + offset[1]
                if inbound(r, c):
                    if board[r][c] == 1:
                        live_neighbor += 1
            return live_neighbor
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    live_neighbor = neighbors(i, j)
                    if live_neighbor < 2 or live_neighbor > 3:
                        dies.add((i, j))
                else:
                    live_neighbor = neighbors(i, j)
                    if live_neighbor == 3:
                        lives.add((i, j))
                        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0 and (i, j) in lives:
                    board[i][j] = 1
                elif board[i][j] == 1 and (i, j) in dies:
                    board[i][j] = 0
                
        
        