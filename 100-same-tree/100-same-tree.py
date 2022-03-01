# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True
        def dsf(node1, node2):
            if node1 and node2:
                if node1.val != node2.val: self.same = False
                dsf(node1.left, node2.left)
                dsf(node1.right, node2.right)
            elif not node1 and not node2:
                return
            else:
                self.same = False
        dsf(p, q)
        return self.same
        