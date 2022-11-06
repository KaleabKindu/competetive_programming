class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = []
        for i in range(n):
            start, end, money = startTime[i], endTime[i], profit[i]
            jobs.append([start, end, money])
            
        jobs.sort()

        @cache
        def dp(job = 0):
            if job >= len(jobs):
                return 0
            
            start, end, profit = jobs[job]
            
            next_job = bisect_left(jobs, end, lo = job + 1, key=lambda x:x[0])
            
            schedule_job = profit + dp(next_job)
            
            skip_job = dp(job + 1)
                
            return max(schedule_job, skip_job)
        
        return dp() 