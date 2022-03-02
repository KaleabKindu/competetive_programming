# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        
        def dsf(root):
            if root:
                if root.left == None and root.right == None:
                    return 1
                left = dsf(root.left)
                right = dsf(root.right)

                if abs(left - right) > 1:
                    self.balanced = False
                return max(left, right) + 1
            return 0
        dsf(root)
        return self.balanced
            