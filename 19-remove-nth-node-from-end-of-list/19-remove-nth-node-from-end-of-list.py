# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = ListNode()
        cur.next = head
        previous = cur
        l = head
        r = head
        for i in range(n):
            r = r.next
        while r:
            previous = l
            l = l.next
            r = r.next
        previous.next = l.next
        l.next = None
        return cur.next
        
            
            
            