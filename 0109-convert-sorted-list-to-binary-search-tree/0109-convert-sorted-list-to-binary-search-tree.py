# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        elements = []
        current_num = head
        while current_num:
            elements.append(current_num.val)
            current_num = current_num.next
        n = len(elements)
        
        def to_BST(i = 0, j = n - 1):
            if i >= j:
                return TreeNode(elements[i]) if i == j else None
            index = (i + j)//2 
            root = TreeNode(elements[index])
            root.left = to_BST(i, index - 1)
            root.right = to_BST(index + 1, j)
            return root
        
        return to_BST()