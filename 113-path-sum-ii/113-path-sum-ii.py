# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        path = []
        def dfs(node = root):
            if node:
                path.append(node.val)
                if not node.left and not node.right:
                    if sum(path) == targetSum:
                        answer.append([*path])
                    path.pop()
                    return
                dfs(node.left)
                dfs(node.right)
                path.pop()
        dfs()
        return answer
