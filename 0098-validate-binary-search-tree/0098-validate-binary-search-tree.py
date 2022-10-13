# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node = root, lo = float('-inf'), hi = float('inf')):
            if node:
                if not lo < node.val < hi:
                    return False
                left = validate(node.left, lo, node.val)
                right = validate(node.right, node.val, hi)
                return left and right
            return True
        return validate()
                