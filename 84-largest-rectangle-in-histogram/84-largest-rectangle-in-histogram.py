class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        area = 0
        for i in range(n):
            indx = i
            while stack and stack[-1][1] > heights[i]:
                index, val = stack.pop()
                area = max(area, (i - index) * val)
                indx  = index
            stack.append((indx, heights[i]))
            
        while stack:
            index, val = stack.pop()
            area = max(area, (n - index) * val)
            
        return area