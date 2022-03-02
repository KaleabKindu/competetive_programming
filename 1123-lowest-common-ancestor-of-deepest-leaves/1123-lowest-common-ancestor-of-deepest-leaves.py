# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.maxdepth = 0
        self.lca = None
        def dsf(node, depth = -1):
            if node:
                depth += 1
                if depth > self.maxdepth:
                    self.maxdepth = depth
                left_depth = dsf(node.left, depth)
                right_depth = dsf(node.right, depth)
                
                if left_depth == right_depth and left_depth >= self.maxdepth:
                    self.lca = node
                
                return max(left_depth, right_depth) 
            return depth
            
        dsf(root)
        return self.lca
    
    
    
    
           