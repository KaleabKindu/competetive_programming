# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def tilt(root):
            if root:
                leftsum = tilt(root.left)
                
                rightsum = tilt(root.right)
                
                self.total += abs(leftsum - rightsum)
                
                return root.val + leftsum + rightsum
            else:
                return 0
                
                
        tilt(root)
        return self.total
                
                
                
            