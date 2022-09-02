# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        path = []
        def dfs(node):
            if node:
                good = True
                for ancestor in path:
                    if ancestor > node.val:
                        good = False
                
                path.append(node.val)
                left = dfs(node.left)
                right = dfs(node.right)
                path.pop()
                return 1 + left + right if good else left + right
            return 0
        
        return dfs(root)