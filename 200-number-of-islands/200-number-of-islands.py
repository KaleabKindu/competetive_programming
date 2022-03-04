class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        R, C = len(grid), len(grid[0])
        in_bound = lambda row, col: 0 <= row <= R - 1 and 0 <= col <= C - 1 
    
        visited = [[False for _ in range(C)] for _ in range(R)]
        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        def isvalid(rw, cn):
            return in_bound(rw, cn) and not visited[rw][cn] \
                    and grid[rw][cn] == "1"
        def dfs(rw, cn):
            visited[rw][cn] = True
            if grid[rw][cn] == "1":
                for direction in DIR:
                    new_rw, new_cn = rw + direction[0], cn + direction[1]
                    if isvalid(new_rw, new_cn):
                        dfs(new_rw, new_cn)
        
        islands = 0
        for i in range(R):
            for j in range(C):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
            
        return islands     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         R, C = len(board), len(board[0])
#         self.region = set()
#         def dfs(rw, cn):
#             if board[rw][cn] == "O":
#                 self.region.add((rw, cn))
#                 if in_bound(rw + 1, cn) and (rw + 1, cn) not in self.region: dfs(rw + 1, cn)
#                 if in_bound(rw - 1, cn) and (rw - 1, cn) not in self.region: dfs(rw - 1, cn)
#                 if in_bound(rw, cn + 1) and (rw, cn + 1) not in self.region: dfs(rw, cn + 1)
#                 if in_bound(rw, cn - 1) and (rw, cn - 1) not in self.region: dfs(rw, cn - 1) 
#         in_bound = lambda row, col: 0 <= row <= R - 1 and 0 <= col <= C - 1 
#         for i in range(len(board[0])):
#             if board[0][i] == "O":
#                 dfs(0, i) 
#         for i in range(len(board[0])):
#             if board[R - 1][i] == "O":
#                 dfs(R - 1, i)
#         for i in range(R):
#             if board[i][0] == "O":
#                 dfs(i, 0)
#         for i in range(R):
#             if board[i][C - 1] == "O":
#                 dfs(i, C - 1)
#         for i in range(R):
#             for j in range(C):
#                 if (i, j) not in self.region and board[i][j] == "O":
#                     board[i][j] = "X"
        
        
        