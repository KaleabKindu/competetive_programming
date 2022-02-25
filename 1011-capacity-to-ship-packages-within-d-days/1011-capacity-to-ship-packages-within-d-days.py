class Solution:
    def helper(self,capacity, weights):
            stak = []
            for i in range(len(weights)):
                if stak == []:
                    stak.append(weights[i])
                elif stak[-1] + weights[i] <= capacity:
                    stak.append(stak.pop()+weights[i])
                else:
                    stak.append(weights[i])
            return len(stak)
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        while start <= end:
            mid = (start + end)//2
            temp = self.helper(mid, weights)
            if temp > days:
                start = mid + 1
            elif temp < days:
                ans=mid
                end = mid - 1
            else:
                ans = mid
                end = mid - 1
        return ans
                    
                
                
            