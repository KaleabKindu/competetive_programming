class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        Found = False
        while start <= end:
            mid = (start + end)//2
            if matrix[mid][0] > target:
                end = mid - 1
            elif matrix[mid][0] <= target <=  matrix[mid][-1]:
                searchRow = matrix[mid]
                Found = True
                break
            else:
                start = mid + 1
        if not Found:
            return False
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
            
                
                