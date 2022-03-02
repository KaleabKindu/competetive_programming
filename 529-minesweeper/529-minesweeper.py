class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R, C = len(board), len(board[0])
        
        self.revealed = set()
        self.countmine = 0
        def nomine(rw, cn):
            mine = True
            for direction in DIR:
                new_rw, new_cn = rw + direction[0], cn + direction[1]
                if in_bound(new_rw, new_cn) and board[new_rw][new_cn] == "M":
                    self.countmine += 1
                    mine = False
            return mine
        def dfs(rw, cn):
            self.revealed.add((rw, cn))
            if board[rw][cn] == "M":
                board[rw][cn] = "X"
                return     
            elif nomine(rw, cn):
                board[rw][cn] = "B"
                for direction in DIR:
                    new_rw, new_cn = rw + direction[0], cn + direction[1]
                    if in_bound(new_rw, new_cn) and (new_rw, new_cn) not in self.revealed:
                        dfs(new_rw, new_cn)
            else:
                board[rw][cn] = str(self.countmine)
                self.countmine = 0
                

        DIR = [[0,1],[1,0],[-1,0],[0,-1],[-1,1],[1,-1],[-1,-1],[1,1]]
        in_bound = lambda rw, cn: 0 <= rw < R and 0 <= cn < C
        dfs(click[0], click[1])
        
        return board
        