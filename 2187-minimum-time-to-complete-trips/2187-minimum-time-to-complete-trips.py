class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def helper(t):
            total=0
            for i in time:
                total+=t//i
            return total
        start = 1
        end = 10000000 * max(time)
        while start <= end:
            mid = (start + end)//2
            trips = helper(mid)
            if trips < totalTrips:
                start = mid + 1
            elif trips < totalTrips:
                end = mid - 1
            else:
                answer = mid
                end = mid - 1
        return answer
            