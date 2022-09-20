# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, largest = float("-inf")):
            if node:
                left = dfs(node.left, node.val if node.val > largest else largest)
                right = dfs(node.right, node.val if node.val > largest else largest)
                return left + right + 1 if node.val >= largest else left + right
            return 0
                
        return dfs(root)