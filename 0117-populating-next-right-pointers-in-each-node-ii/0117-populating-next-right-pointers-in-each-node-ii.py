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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = deque([root])
        while queue:
            previous = Node()
            for _ in range(len(queue)):
                node = queue.popleft()
                previous.next = node
                previous = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root