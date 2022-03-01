# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.seen = set()
        self.found = False
        def diff(node,k):
            if node:
                diff(node.left, k)
                if node.val in self.seen:
                    self.found = True
                self.seen.add(node.val)
                self.seen.add(k - node.val)
                diff(node.right, k)
        diff(root, k)
        return self.found
        
        