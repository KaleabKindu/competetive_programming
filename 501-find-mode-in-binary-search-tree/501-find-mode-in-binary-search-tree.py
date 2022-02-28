# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root,seen):
        if not root:
            return 
        seen[root.val] = seen.get(root.val, 0) + 1
        self.traverse(root.left, seen)
        self.traverse(root.right, seen)
        return seen
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        trav = self.traverse(root,{})
        temp = sorted(trav.items(), key = lambda x:x[1])
        mode=[]
        md = temp[-1][1]
        for i in range(len(temp)-1,-1,-1):
            if temp[i][1] != md:
                break
            mode.append(temp[i][0])
        return mode
        