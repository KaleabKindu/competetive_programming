# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        prefix = defaultdict(int)
        prefix[0] += 1
        def dfs(node = root, total = 0):
            if node:
                total += node.val
                if total - targetSum in prefix:
                    self.count += prefix[total - targetSum]
                prefix[total] += 1
                dfs(node.left, total)
                dfs(node.right, total)
                prefix[total] -= 1
        dfs()
        return self.count 