class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        self.visited = set()
        def bfs(index):
            queue = deque([index])
            self.visited.add(index)
            while queue:
                currentindex = queue.popleft()
                if arr[currentindex] == 0:
                    return True
                if in_bound(currentindex + arr[currentindex]):
                    queue.append(currentindex + arr[currentindex])
                    self.visited.add(currentindex + arr[currentindex])
                if in_bound(currentindex - arr[currentindex]):
                    queue.append(currentindex - arr[currentindex]) 
                    self.visited.add(currentindex - arr[currentindex])
            return False
        
        in_bound = lambda index: 0 <= index < len(arr) and index not in self.visited
        return bfs(start)
        