class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        
        in_bound = lambda row, col: 0 <= row <= R - 1 and 0 <= col <= C - 1
        DIR = [[0, 1],[1, 0],[0, -1],[-1, 0]]
        
        visited = [[False for _ in range(C)] for _ in range(R) ]
        minHeap = [(0, (0, 0))]
        answer = 0
        while minHeap:
            effort, cell = heappop(minHeap)
            if visited[cell[0]][cell[1]]:
                continue
            visited[cell[0]][cell[1]] = True
            if cell[0] == R - 1 and cell[1] == C - 1:
                answer = effort
            for direction in DIR:
                new_rw, new_cn = cell[0] + direction[0], cell[1] + direction[1]
                if in_bound(new_rw, new_cn) and not visited[new_rw][new_cn]:
                    absdiff = abs(heights[cell[0]][cell[1]] - heights[new_rw][new_cn])
                    heappush(minHeap, (max(absdiff, effort), (new_rw, new_cn)))
            
        return answer