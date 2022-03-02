# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.grandparents = []
        self.totalsum = 0
        def dfs(root):
            if root:
                if len(self.grandparents) > 1 and self.grandparents[-2] % 2 == 0:
                    self.totalsum += root.val
                self.grandparents.append(root.val)
                dfs(root.left)
                dfs(root.right)
                self.grandparents.pop()
        dfs(root)
        return self.totalsum