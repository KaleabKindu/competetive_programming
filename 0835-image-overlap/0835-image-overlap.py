class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n, m = len( img1 ), len( img1[0] )
        # collect ones
        img1_ones = []
        img2_ones = []
        shifts = defaultdict(int)
        shifts[-1] = 0  # starter value to avoid condition
        
        for i in range( n ):
            for j in range( m ):
                if img1[i][j] == 1:
                    img1_ones.append( (i, j) )
                if img2[i][j] == 1:
                    img2_ones.append( (i, j) )
                    
        
        for row1, col1 in img1_ones:
            for row2, col2 in img2_ones:
                required_shift = row1 - row2, col1 -col2
                shifts[required_shift] += 1
                
        return max(shifts.values())