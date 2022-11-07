class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        battleships = 0
        directions = [[0,1],[1,0]]
        in_bound = lambda i, j: 0 <= i < n and 0 <= j < m
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X':
                    count = 0
                    for direction in directions:
                        r, c = i + direction[0], j + direction[1]
                        if in_bound(r, c) and board[r][c] == 'X':
                            count += 1
                    if count == 0:
                        battleships += 1
        
        return battleships