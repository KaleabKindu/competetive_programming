# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def bfs(node = root):
            queue = deque([node])
            count = 0
            while queue:
                if count % 2 != 0:
                    l, r = 0, len(queue) - 1
                    while l < r:
                        queue[l].val, queue[r].val = queue[r].val, queue[l].val
                        l += 1
                        r -= 1
                for i in range(len(queue)):
                    curnode = queue.popleft()
                    if curnode.left:
                        queue.append(curnode.left)
                    if curnode.right:
                        queue.append(curnode.right)
                count += 1
        bfs()
        return root
                
            