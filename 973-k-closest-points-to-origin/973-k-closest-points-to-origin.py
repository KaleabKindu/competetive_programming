import math
class Solution:
    def calc(self,point):
        return math.sqrt(point[0]**2  +  point[1]**2)
    def mergeSort(self,points):
        if len(points) > 1:
            mid = len(points) // 2
            left = points[:mid]
            right = points[mid:]
            self.mergeSort(left)
            self.mergeSort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if self.calc(left[i]) <= self.calc(right[j]):
                    points[k] = left[i]
                    i += 1
                else:
                    points[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                points[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                points[k]=right[j]
                j += 1
                k += 1
        return points

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.mergeSort(points)
        return points[:k]
        