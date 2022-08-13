class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        def shift(index):
            new = 0
            while index < len(arr):
                arr[index], new = new, arr[index]
                index += 1
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                shift(i + 1)
                i += 2
            else:
                i += 1
            
                