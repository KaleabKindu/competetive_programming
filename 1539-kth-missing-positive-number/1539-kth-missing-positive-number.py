class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def helper(target):
            start = 0
            end = len(arr) - 1
            while start <= end:
                mid = (start + end)//2
                if arr[mid] < target:
                    start = mid + 1
                elif arr[mid] > target:
                    end = mid - 1
                else:
                    return True
            return False
        answer = []
        i = 1
        while len(answer) < k:
            if not helper(i):
                answer.append(i)
            i+=1
        print(i)
        return answer[-1]
            
            
            
            