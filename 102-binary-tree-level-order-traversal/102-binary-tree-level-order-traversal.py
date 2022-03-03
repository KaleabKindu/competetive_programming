# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        self.answer = []
        def bfs(root):
            queue = deque([root])
            while queue:
                current_level = []
                for i in range(len(queue)):
                    current = queue.popleft()
                    current_level.append(current.val)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                self.answer.append(current_level)
        bfs(root) 
        return self.answer 
        