class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.visited = set()
        self.queue = collections.deque()
        self.minute = 0
        def valid(rw, cn):
            return (in_bound(rw, cn)) and ((rw, cn) not in self.visited )\
                and (grid[rw][cn] == 1)
      
        def bfs():
            while self.queue:
                for i in range(len(self.queue)):
                    x, y = self.queue.popleft()
                    for direction in DIR:
                        new_rw, new_cn = x + direction[0], y + direction[1]
                        if valid(new_rw, new_cn):
                            grid[new_rw][new_cn] = 2
                            self.visited.add((new_rw, new_cn))
                            self.queue.append((new_rw, new_cn))
                if self.queue:
                    self.minute += 1

        in_bound = lambda row, col : 0 <= row < R and 0 <= col < C
        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        
        for i in range(R):
            for j in range(C):
                if (i, j)not in self.visited  and grid[i][j] == 2:
                    self.queue.append((i, j))
        bfs()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return -1
        return self.minute