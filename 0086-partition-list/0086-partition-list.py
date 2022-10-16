# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        answer = left = ListNode()
        _right = right = ListNode()
        cur = head
        while cur:
            if cur.val >= x:
                right.next = cur
                right = cur
            else:
                left.next = cur
                left = cur
            cur = cur.next
        left.next = _right.next
        right.next = None
        return answer.next
                
                
                