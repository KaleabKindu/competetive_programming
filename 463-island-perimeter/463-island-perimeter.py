class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        valid = lambda row, col: 0 <= row < n and 0 <= col < m and grid[row][col] == 1
        DIR = [(1,0),(0, 1),(-1,0),(0,-1)]
        visited = set()
        
        def dfs(i, j):            
            visited.add((i, j))
            perimeter = 4
            count = 0
            for direction in DIR:
                nrow, ncol = direction[0] + i, direction[1] + j
                if valid(nrow, ncol):
                    count += 1
            perimeter -= count
            for direction in DIR:
                nrow, ncol = direction[0] + i, direction[1] + j
                if valid(nrow, ncol) and (nrow, ncol) not in visited:
                    perimeter += dfs(nrow, ncol) 
            
            return perimeter 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
                     
                
                
                
#   Time Complexity = O(row * col)
#   Space Complexity = O(row * col)
       
        