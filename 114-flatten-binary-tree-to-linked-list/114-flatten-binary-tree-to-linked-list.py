# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.link = deque()
        def dfs(node):
            if node:
                self.link.append(node)
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)  
        while self.link:
            temp = self.link.popleft()
            if not self.link:
                temp.right = None
                break
            temp.right = self.link[0]
            temp.left = None
        return root