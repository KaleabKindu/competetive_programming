class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.visited = set()
        def flood(sr,sc):
            if (sr,sc) not in self.visited:
                color = image[sr][sc]
                image[sr][sc] = newColor
                self.visited.add((sr,sc))
                if sc + 1 < len(image[0]) and image[sr][sc + 1] == color:
                    flood( sr, sc + 1)
                if sc - 1 >= 0 and image[sr][sc - 1] == color:
                    flood(sr, sc - 1 )
                if sr + 1 < len(image) and image[sr + 1][sc] == color:
                    flood(sr + 1, sc)
                if sr - 1 >= 0 and image[sr - 1][sc] == color:
                    flood(sr - 1, sc)
        flood(sr,sc)
        return image
        
        
