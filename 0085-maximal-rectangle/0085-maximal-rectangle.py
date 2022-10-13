class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        def rectangle(heights):
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
        heights = [[0]* m for i in range(n)]
        answer = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    heights[i][j] += 1 + heights[i - 1][j]
        for i in range(n):
            answer = max(answer, rectangle(heights[i]))
        return answer