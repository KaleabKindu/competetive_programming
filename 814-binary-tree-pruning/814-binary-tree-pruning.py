# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node = root):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                if not left:
                    node.left = None
                if not right:
                    node.right = None
                if node.val == 1:
                    return True
                return False or right or left
            return False
        
        if not dfs():
            return None
            
        return root