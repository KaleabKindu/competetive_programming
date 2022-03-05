# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        answer = deque()
        def bfs(root):
            queue = deque([root])
            while queue:
                currentLevel = []
                for i in range(len(queue)):
                    current = queue.popleft()
                    currentLevel.append(current.val)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                answer.appendleft(currentLevel)
        bfs(root)
        return answer 
                    
            
        