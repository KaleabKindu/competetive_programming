class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        Matrix=[]
        for i in matrix:
            Matrix.extend(i)
        Matrix.sort()
        return Matrix[k-1]