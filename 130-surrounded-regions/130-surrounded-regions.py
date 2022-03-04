class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        self.region = set()
        def dfs(rw, cn):
            if board[rw][cn] == "O":
                self.region.add((rw, cn))
                if in_bound(rw + 1, cn) and (rw + 1, cn) not in self.region: dfs(rw + 1, cn)
                if in_bound(rw - 1, cn) and (rw - 1, cn) not in self.region: dfs(rw - 1, cn)
                if in_bound(rw, cn + 1) and (rw, cn + 1) not in self.region: dfs(rw, cn + 1)
                if in_bound(rw, cn - 1) and (rw, cn - 1) not in self.region: dfs(rw, cn - 1) 
        in_bound = lambda row, col: 0 <= row <= R - 1 and 0 <= col <= C - 1 
        for i in range(len(board[0])):
            if board[0][i] == "O":
                dfs(0, i) 
        for i in range(len(board[0])):
            if board[R - 1][i] == "O":
                dfs(R - 1, i)
        for i in range(R):
            if board[i][0] == "O":
                dfs(i, 0)
        for i in range(R):
            if board[i][C - 1] == "O":
                dfs(i, C - 1)
        for i in range(R):
            for j in range(C):
                if (i, j) not in self.region and board[i][j] == "O":
                    board[i][j] = "X"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 
                
