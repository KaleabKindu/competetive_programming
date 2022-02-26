class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(searchRow):
            start = 0
            end = len(searchRow) - 1
            while start <= end:
                mid = (start + end)//2
                if searchRow[mid] < target:
                    start = mid + 1
                elif searchRow[mid] > target:
                    end = mid - 1
                else:
                    return True
            return False
        for i in matrix:
            if helper(i):
                return True
        return False
        
        