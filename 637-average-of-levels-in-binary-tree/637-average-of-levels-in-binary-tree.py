# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.answer = []
        def bsf(root):
            queue = collections.deque([root])
            while queue:
                total = 0
                for node in queue:
                    total += node.val
                self.answer.append(total/len(queue))
                for i in range(len(queue)):
                    current = queue.popleft()
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)                              
        bsf(root)
        return self.answer