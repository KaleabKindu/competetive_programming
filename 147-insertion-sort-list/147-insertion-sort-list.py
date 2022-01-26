# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        temp=ListNode(-5001)
        temp.next=ListNode(cur.val)
        cur=cur.next
        while cur:
            start=temp
            while start and start.val < cur.val:
                prev=start
                start=start.next
            if not start:
                prev.next=ListNode(cur.val)
                prev.next.next=None
            else:
                prev.next=ListNode(cur.val)
                prev.next.next=start
            cur=cur.next
            
        return temp.next
    
                
            
        