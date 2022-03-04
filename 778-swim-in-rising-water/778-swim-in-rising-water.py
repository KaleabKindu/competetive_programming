class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        in_bound = lambda row, col : 0 <= row < R and 0 <= col < C
        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        
        minHeap = [(grid[0][0], (0, 0))]
        t = 0
        visited = [[False for x in range(C)] for _ in range(R)]
        while minHeap:
            elevation, cell = heappop(minHeap)
            if visited[cell[0]][cell[1]]:
                continue
            t = max(t, elevation)
            if cell[0] == R - 1 and cell[1] == C - 1:
                break
            visited[cell[0]][cell[1]] = True
            
            for direction in DIR:
                new_rw, new_cn = cell[0] + direction[0], cell[1] + direction[1]
                if in_bound(new_rw, new_cn):
                    heappush(minHeap,(grid[new_rw][new_cn], (new_rw, new_cn)))
        return t
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
