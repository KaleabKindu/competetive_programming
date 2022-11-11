class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        
        changed.sort()
        
        doubled = []
        
        queue = deque()
        
        for i in range(n):
            if not queue:
                queue.append(changed[i])
            elif changed[i] / 2 == queue[0]:
                doubled.append(queue.popleft())
            else:
                queue.append(changed[i])
                
        return doubled if len(doubled) == (len(changed)//2) else []
            