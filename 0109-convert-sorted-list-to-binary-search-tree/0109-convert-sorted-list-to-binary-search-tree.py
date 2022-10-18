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
        def middle_node(node):
            slow = node
            fast = node
            prev = node
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return slow
        def to_BST(node = head):
            if not node:
                return None
            if not node.next:
                return TreeNode(node.val)
            middle = middle_node(node)
            root = TreeNode(middle.val)
            root.left = to_BST(node) 
            root.right = to_BST(middle.next) 
            return root
        
        return to_BST()