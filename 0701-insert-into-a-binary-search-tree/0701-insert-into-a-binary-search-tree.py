# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        answer = TreeNode(0,root)
        def searchBST(node = root):
            if node:
                if val < node.val:
                    node.left = searchBST(node.left)
                if val > node.val:
                    node.right = searchBST(node.right)
                return node
            return TreeNode(val)
        answer.left = searchBST()
        return answer.left