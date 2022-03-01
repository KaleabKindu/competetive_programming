# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.total = 0
        self.bool = False
        def path(node):
            if node:
                self.total += node.val
                if node.left == None and node.right == None:
                    if self.total == targetSum:
                        self.bool = True
                path(node.left)
                path(node.right)
                self.total -= node.val
        path(root)
        return self.bool
                
            
        