"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.maxdepth = 0
        self.depth = 0
        def depth(node):
            if not node:
                return
            self.depth += 1
            if node.children!=[] : 
                for i in node.children:
                    depth(i) 
                    self.depth -= 1 
            else:
                self.maxdepth = max(self.maxdepth,self.depth)
        
        depth(root)
        return self.maxdepth
        
            
        
        