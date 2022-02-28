# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int, total = 0) -> int:
        self.total = 0
        def Inorder(node):
            if node: 
                if node.val >= low and node.val <= high:
                    self.total += node.val 
                if low < node.val:
                    Inorder(node.left)
                if high > node.val:
                    Inorder(node.right)
        Inorder(root)
        return self.total
            
        
        
        
        
        
        
        
        
        
        
#         if not root:
#             return total
#         if low <= root.val <= high:
#             total += root.val
#         print(total)
#         self.rangeSumBST(root.left, low, high, total)
#         self.rangeSumBST(root.right, low, high, total)
#         # return total
        