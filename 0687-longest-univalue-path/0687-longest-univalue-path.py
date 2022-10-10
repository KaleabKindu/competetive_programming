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
                if left[0] == right[0] == node.val:
                    self.answer = max(self.answer, left[1] + right[1])
                    return node.val, max(left[1], right[1]) + 1
                elif left[0] == node.val:
                    self.answer = max(self.answer, right[1]-1)
                    return node.val, left[1] + 1
                elif right[0] == node.val:
                    self.answer = max(self.answer, left[1]-1)
                    return node.val, right[1] + 1
                else:
                    self.answer = max(self.answer, left[1] - 1, right[1] - 1)
                    return node.val, 1
                    
            return "", 0
        if root: self.answer= max(dfs()[1]-1,self.answer)
        return self.answer
                
                
            