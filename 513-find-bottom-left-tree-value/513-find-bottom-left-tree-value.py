# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):
            queue = deque([root])
            while queue:
                currentLevel = []
                for i in range(len(queue)):
                    current = queue.popleft()
                    currentLevel.append(current.val)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                        
            return currentLevel[0]
        
        return bfs(root)
                