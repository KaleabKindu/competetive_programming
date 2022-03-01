# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dsf(root):
            if root:
                root.left, root.right = root.right, root.left
                dsf(root.left)
                dsf(root.right)
                
        dsf(root)
        return root