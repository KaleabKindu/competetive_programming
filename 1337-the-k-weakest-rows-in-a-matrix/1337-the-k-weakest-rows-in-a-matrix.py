class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count += 1
                else:
                    break
            heappush(heap, (count, i))
        answer = []
        for i in range(k):
            answer.append(heappop(heap)[1])
        return answer