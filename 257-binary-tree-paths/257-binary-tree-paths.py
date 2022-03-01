# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.answer = []
        def dsf(root, path = ""):
            if root:
                if root.left == None and root.right == None:
                    self.answer.append(path + str(root.val))
                path += str(root.val) + "->"
                dsf(root.left, path)
                dsf(root.right, path)
              
        dsf(root)
        return self.answer
        