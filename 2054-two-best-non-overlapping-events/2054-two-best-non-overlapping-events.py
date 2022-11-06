class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        
        @cache
        def dp(event = 0, attended = 0):
            if event >= n or attended == 2:
                return 0
            start, end, value = events[event]
            
            next_event = bisect_left(events, end + 1, lo = event + 1, key=lambda x:x[0])
            
            attend = value + dp(next_event, attended + 1)
            
            skip_event = dp(event + 1, attended)
            
            return max(attend, skip_event)
        
        return dp()