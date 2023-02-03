# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        columns = defaultdict(list)
        def dfs(node = root, row = 0, col = 0):
            if node:
                columns[col].append((row, node.val))
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)
        dfs()
        cols = sorted(columns)
        answer = []
        for key in cols:
            col = []
            for row, val in sorted(columns[key]):
                col.append(val)
            answer.append(col)
        return answer