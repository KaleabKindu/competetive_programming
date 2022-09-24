# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        def dfs(node = root, number = 0):
            if node:
                num = (10 * number) + node.val
                if not node.right and not node.left:
                    self.total += num
                    return
                dfs(node.left, num)
                dfs(node.right, num)
        
        dfs()
        return self.total