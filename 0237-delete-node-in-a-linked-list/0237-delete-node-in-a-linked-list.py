# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        def helper(root = node):
            if not root.next:
                return None
            root.val = root.next.val
            root.next = helper(root.next)
            return root
        helper()