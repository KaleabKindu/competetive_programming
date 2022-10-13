# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        answer = TreeNode(0,root)
        def searchBST(node, val):
            if node:
                if val < node.val:
                    node.left = searchBST(node.left, val)
                if val > node.val:
                    node.right = searchBST(node.right, val)
                return node
            return TreeNode(val)
        answer.left = searchBST(root, val)
        return answer.left