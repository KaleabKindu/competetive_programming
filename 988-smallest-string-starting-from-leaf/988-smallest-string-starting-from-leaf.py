# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        strings = []
        path = deque()
        def dfs(node = root):
            if node:
                path.appendleft(chr(97 + node.val)) 
                if not node.left and not node.right:
                    strings.append("".join([*path]))
                    path.popleft()
                    return
                dfs(node.left)
                dfs(node.right)
                path.popleft()
                
        dfs()
        strings = sorted(strings)
        return strings[0]
        