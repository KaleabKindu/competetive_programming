class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def getRow(index):
            if index == 0:
                return [1]
            previous = getRow(index - 1)
            row = [1] * (len(previous) + 1)
            for i in range(1, len(row) - 1):
                row[i] = previous[i] + previous[i - 1]
            return row
        return getRow(rowIndex)