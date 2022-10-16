class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n = len(arr)
        arr.sort()
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
                    
                    left = 0
                    num = arr[j]
                    while arr[j] == num:
                        j += 1
                        left += 1

                    right = 0
                    num = arr[k]
                    while arr[k] == num:
                        k -= 1
                        right += 1

                    answer += left * right
                        
        return answer % (10**9 + 7)
                
                
                