"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        visited = set()
        def dfs(node,  depth = 1):
            visited.add(node)
            maxdepth = depth
            for child in node.children:
                if child not in visited:
                    maxdepth = max(maxdepth, dfs(child, depth + 1))
                    
            return maxdepth 
        
        return dfs(root) if root else 0
        
            
        
        