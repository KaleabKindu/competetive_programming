
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w = len(word)
        n, m = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        valid = lambda r, c: 0 <= r < n and 0 <= c < m and board[r][c] == word[self.k]  and not visited[r][c]
        visited = [[False]*m for i in range(n)]
        self.k = 0
        
        boardCount = defaultdict(int)
        for i in range(n):
            for j in range(m):
                boardCount[board[i][j]] += 1
        for char in word:
            if word.count(char) > boardCount[char]:
                return False
        
        def bk(i, j):
            if self.k >= w:
                return True
            for direction in directions:
                r, c = i + direction[0], j + direction[1]
                if valid(r, c):
                    visited[r][c] = True
                    self.k += 1
                    if bk(r, c): return True
                    self.k -= 1
                    visited[r][c] = False
            return False
    
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[self.k]:
                    visited[i][j] = True
                    self.k += 1
                    if bk(i, j): return True
                    visited[i][j] = False
                    self.k -= 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                            
        
                    
                    