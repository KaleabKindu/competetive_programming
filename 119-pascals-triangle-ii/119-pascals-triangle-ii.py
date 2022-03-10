class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = [[1]]
        index = 0
        for i in range(34):
            index += 1
            row = [1] * (len(res[-1]) + 1)
            for j in range(1, len(row) - 1):
                row[j] = res[-1][j] + res[-1][j - 1]
            if index == rowIndex:
                return row
            res.append(row)
        
