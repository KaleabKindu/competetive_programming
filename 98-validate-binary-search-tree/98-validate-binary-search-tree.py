# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validator(self, node, lower, upper):
        if not node:
            return True
        if not lower < node.val < upper:
            return False
        left = self.validator(node.left, lower, node.val)
        right = self.validator(node.right, node.val, upper)
        return left and right
     
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower, upper = -float("inf"), float("inf")
        return self.validator(root,lower,upper)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not root.left and not root.right:
        #     return True
        # elif not root.left and root.right:
        #     if root.val>=root.right.val:
        #         return False
        #     return self.isValidBST(root.right)
        # elif not root.right and root.left:
        #     if root.val<=root.left.val:
        #         return False
        #     return self.isValidBST(root.left)
        # else:
        #     if root.val <= root.left.val or root.val >= root.right.val:
        #         return False
        #     right=self.isValidBST(root.right)
        #     left=self.isValidBST(root.left)
        #     return right and left
                
        
        
        