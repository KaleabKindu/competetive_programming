# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []
        def dsf_left(root):
            if root:
                dsf_left(root.left)
                left.append(root.val)
                dsf_left(root.right)
            left.append(0)
        def dsf_right(root):
            if root:
                dsf_right(root.right)
                right.append(root.val)
                dsf_right(root.left)
            right.append(0)
        dsf_right(root)
        dsf_left(root)
        for i in range(len(left)):
            if left[i] != right[i]:
                return False
        return True
        
            
       