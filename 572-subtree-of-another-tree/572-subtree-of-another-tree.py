# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(node1, node2):
            if node1 and node2:
                left  = equal(node1.left, node2.left)
                right  = equal(node1.right, node2.right)
                return node1.val == node2.val and left and right
            return True if not node1 and not node2 else False
        
        def dfs(node = root):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                return equal(node, subRoot) or left or right if node.val == subRoot.val else left or right
            return False
        return dfs()