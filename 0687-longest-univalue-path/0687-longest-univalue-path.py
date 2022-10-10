# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def dfs(node = root):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                left_length = right_length = 0
                if node.left and node.left.val == node.val:
                    left_length = left + 1
                if node.right and node.right.val == node.val:
                    right_length = right + 1
                self.answer = max(self.answer, left_length + right_length)
                return max(left_length, right_length)
            return 0
        dfs()
        return self.answer
                
                
            