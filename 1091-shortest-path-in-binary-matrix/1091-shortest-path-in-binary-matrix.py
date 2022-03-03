class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.visited = [[False for x in range(C)] for _ in range(R)]
        def valid(rw, cn):
            return in_bound(rw, cn) and not self.visited[rw][cn] \
                and grid[rw][cn] == 0
        def bfs(rw, cn):
            queue = deque()
            queue.append((rw, cn, 1))
            self.visited[rw][cn] = True
            while queue:
                current = queue.popleft()
                if current[0] == R - 1 and current[1] == C - 1:
                    return current[2]
                for direction in DIR:
                    new_rw, new_cn = current[0] + direction[0], current[1] + direction[1]
                    if valid(new_rw, new_cn):
                        self.visited[new_rw][new_cn] = True
                        queue.append((new_rw, new_cn, current[2] + 1))    
            return -1
        in_bound = lambda row, col : 0 <= row < R and 0 <= col < C
        DIR = [[0,1],[1,0],[-1,0],[0,-1],[-1,1],[1,-1],[-1,-1],[1,1]]

        
        return bfs(0, 0) if grid[0][0] == 0 else -1