# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        answer = ListNode()
        
        def recurse(node):
            if node.next == None:
                answer.next = node
                return node
            temp = recurse(node.next)
            temp.next = node
            return node
        temp = recurse(head)
        temp.next = None
        return answer.next