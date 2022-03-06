"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        def bfs(root):
            queue = deque([root])
            output = []
            while queue:
                currentLevel = []
                for i in range(len(queue)):
                    current = queue.popleft()
                    currentLevel.append(current.val)
                    for child in current.children:
                        queue.append(child)
                output.append(currentLevel)
            return output
        
        return bfs(root) if root else root