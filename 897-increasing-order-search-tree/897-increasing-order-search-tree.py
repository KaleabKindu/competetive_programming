# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        heap = []
        def traverse(root):
            if root:
                traverse(root.left)
                heappush(heap, (root.val, root))
                traverse(root.right)
        traverse(root)
        dummy = prev = TreeNode()
        while heap:
            prev.right = heappop(heap)[1]
            prev = prev.right
            prev.left = None
        return dummy.right
            
        
            
            
        
