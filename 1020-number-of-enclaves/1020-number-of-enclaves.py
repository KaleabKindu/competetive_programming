class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.region = set()
        def dfs(rw, cn):
            if grid[rw][cn] == 1:
                self.region.add((rw, cn))
                if in_bound(rw + 1, cn) and (rw + 1, cn) not in self.region: dfs(rw + 1, cn)
                if in_bound(rw - 1, cn) and (rw - 1, cn) not in self.region: dfs(rw - 1, cn)
                if in_bound(rw, cn + 1) and (rw, cn + 1) not in self.region: dfs(rw, cn + 1)
                if in_bound(rw, cn - 1) and (rw, cn - 1) not in self.region: dfs(rw, cn - 1) 
        in_bound = lambda row, col: 0 <= row <= R - 1 and 0 <= col <= C - 1 
        for i in range(len(grid[0])):
            if grid[0][i] == 1:
                dfs(0, i) 
        for i in range(len(grid[0])):
            if grid[R - 1][i] == 1:
                dfs(R - 1, i)
        for i in range(R):
            if grid[i][0] == 1:
                dfs(i, 0)
        for i in range(R):
            if grid[i][C - 1] == 1:
                dfs(i, C - 1)
        count = 0
        for i in range(R):
            for j in range(C):
                if (i, j) not in self.region and grid[i][j] == 1:
                    count += 1
        return count