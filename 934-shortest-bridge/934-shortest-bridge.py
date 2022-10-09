class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        in_bound = lambda i, j: 0 <= i < n and 0 <= j < m
        visited = [[False]*m for i in range(n)]
        path = set()
        def dfs(i, j):
            path.add((i, j))
            for direction in directions:
                r, c = i + direction[0], j + direction[1]
                if in_bound(r,c) and not visited[r][c] and grid[r][c] == 1 :
                    visited[r][c] = True
                    dfs(r,c)
        lands = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)
                    lands.append(path.copy())
                    path.clear()
        land1, land2 = set(lands[0]), set(lands[1])
        queue = deque()
        _visited = [[False]*m for i in range(n)]
        for r, c in land1:
            queue.append((r, c, 0))
            _visited[r][c] = True

        
        while queue:
            r, c, bridge = queue.popleft()
            if (r, c) in land2:
                return bridge - 1
            for direction  in directions:
                nr, nc = r + direction[0], c + direction[1]
                if in_bound(nr, nc) and not _visited[nr][nc]:
                    _visited[nr][nc] = True
                    queue.append((nr, nc, bridge if (nr, nc) in land1 else bridge + 1) )