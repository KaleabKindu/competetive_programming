class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n = len(arr)
        arr.sort()
        rightmost = defaultdict(int)
        leftmost = defaultdict(int)
        for i in range(n):
            rightmost[arr[i]] = i
        for i in range(n - 1, -1, -1):
            leftmost[arr[i]] = i
        answer = 0
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                total = arr[i] + arr[j] + arr[k]
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    if arr[j] == arr[k]:
                        m =  k - j + 1
                        answer += factorial(m)//(2 * factorial(m - 2))
                        break
                    left = rightmost[arr[j]] - j + 1
                    right = k - leftmost[arr[k]] + 1
                    j = rightmost[arr[j]] + 1
                    k = leftmost[arr[k]] - 1
                
                    answer += left * right
                        
        return answer % (10**9 + 7)
                
                
                