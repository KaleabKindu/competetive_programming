class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        isvalid = lambda row, col: 0 <= row < R  and  0 <= col < C and not visited[row][col] 
        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        
        queue = collections.deque([(sr, sc)])
        visited = [[False for _ in range(C)] for _ in range(R)]
        color = image[sr][sc] 
        while queue:
            row, col = queue.popleft()
            image[row][col] = newColor
            for direction in DIR:
                new_row, new_col = row + direction[0], col + direction[1]
                if isvalid(new_row, new_col) and image[new_row][new_col] == color:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))
        
        return image
            
        
        
