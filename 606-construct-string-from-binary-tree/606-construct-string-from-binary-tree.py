# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = []
        def dfs(node = root):
            if node:
                string.append(str(node.val))
                
                if node.left and node.right:
                    string.append('(')
                    dfs(node.left)
                    string.append(')')
                    string.append('(')
                    dfs(node.right)
                    string.append(')')
                elif node.left or node.right:
                    string.append('(')
                    dfs(node.left)
                    string.append(')')
                    if node.right:
                        string.append('(')
                        dfs(node.right)
                        string.append(')')
               
            return ""
        dfs()
        return "".join(string)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         string = []
        
#         def dfs(node = root):
#             if node:
                
#                 left = dfs(node.left)
#                 right = dfs(node.right)
#                 if left and right:
#                     return str(node.val) + '(' + left + ')' + '('+ right + ')'
#                 elif left:
#                     return str(node.val) + '(' + left + ')' 
#                 else:
#                      return str(node.val) + '(' + right + ')' 
#             return ""
#         return dfs()