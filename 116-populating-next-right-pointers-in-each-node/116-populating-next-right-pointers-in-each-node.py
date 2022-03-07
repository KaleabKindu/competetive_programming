"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        def bfs(root):
            queue = deque([root])
            while queue:
                currentLevel = deque()
                for i in range(len(queue)):
                    current = queue.popleft()
                    currentLevel.append(current)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                while currentLevel:
                    temp = currentLevel.popleft()
                    if currentLevel:
                        temp.next = currentLevel[0]
                    else:
                        temp.next = None
        bfs(root)
        return root
                    
        