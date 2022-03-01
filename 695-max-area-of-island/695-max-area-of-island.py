class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.visited = set()
        self.maxarea = 0
        self.area = 0
        def dfs(rw, cn):
            self.visited.add((rw, cn))
            self.area += 1
            
            if rw + 1 < R and grid[rw + 1][cn] == 1:
                if (rw + 1, cn) not in self.visited:
                    dfs(rw + 1, cn)
            if rw - 1 >= 0 and grid[rw - 1][cn] == 1:
                if (rw - 1, cn) not in self.visited:
                    dfs(rw - 1, cn)
            if cn + 1 < C and grid[rw][cn + 1] == 1:
                if (rw, cn + 1) not in self.visited:
                    dfs(rw, cn + 1)
            if cn - 1 >= 0 and grid[rw][cn - 1] == 1:
                if (rw, cn - 1) not in self.visited:
                    dfs(rw, cn - 1)
            
        for i in range(R):
            for j in range(C):
                if (i, j) not in self.visited and grid[i][j] == 1:
                    print(i,j)
                    dfs(i, j)
                    self.maxarea = max(self.maxarea, self.area)
                    self.area = 0
        return self.maxarea
                    
                
                