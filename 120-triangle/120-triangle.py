class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = {}
        def triang(index, row):
            if row >= len(triangle):
                return 0
            if (index, row) in  dp:
                return dp[(index, row)]
            else:
                Bleft = triangle[row][index] + triang(index, row + 1)

                Bright = triangle[row][index] + triang(index + 1, row + 1)

                dp[(index, row)] = min(Bright, Bleft)
                
            return dp[(index, row)]
        
        return triang(0, 0)
            
        