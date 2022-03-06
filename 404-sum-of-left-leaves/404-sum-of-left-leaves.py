# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def dfs(node, label = ""):
            if node:
                if node.left == None and node.right == None:
                    if label == "left":
                        self.total += node.val
                dfs(node.left, "left")
                dfs(node.right, "right")
        
        dfs(root)
        return self.total
                
        