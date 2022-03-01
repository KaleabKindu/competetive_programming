# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.mindepth = float("inf")
        def dsf(root, depth = 0):
            if root:
                if root.left == None and root.right == None:
                    self.mindepth = min(self.mindepth, depth + 1)
                depth += 1
                dsf(root.left, depth)
                dsf(root.right, depth)
        dsf(root)
        return self.mindepth if root else 0