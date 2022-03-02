# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        superroot = root
        low = TreeNode(-float("inf"))
        high = TreeNode(float("inf"))
        def dfs(root, lower, upper):
            if root:
                if not lower.val < root.val < upper.val:
                    if root.val < lower.val:
                        root.val, lower.val = lower.val, root.val
                    elif root.val > upper.val:
                        root.val, upper.val = upper.val, root.val
                    dfs(superroot, low, high)
                dfs(root.left, lower, root)
                dfs(root.right, root, upper)
        
        dfs(root, low, high)