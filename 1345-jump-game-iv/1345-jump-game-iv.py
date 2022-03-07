class Solution:
    def minJumps(self, arr: List[int]) -> int:
        isValid = lambda index: 0 <= index < len(arr) and index not in visited
        
        position = defaultdict(set)
        
        left = right = 0
        while right < len(arr):
            if arr[right] == arr[left]:
                right += 1
            else:
                position[arr[left]].add(left)
                position[arr[left]].add(right - 1)
                left = right
        position[arr[left]].add(right - 1)
        
        visited = {0}
        queue = deque([(0, 0)])
        while queue:
            current, move = queue.popleft()
            if current == len(arr) - 1:
                return move
            if isValid(current + 1):
                visited.add(current + 1)
                queue.append((current + 1, move + 1))
            if isValid(current - 1):
                visited.add(current - 1)
                queue.append((current - 1, move + 1))
            for child in position[arr[current]]:
                if child not in visited:
                    queue.append((child, move + 1))
            position[arr[current]].clear()   
                
            