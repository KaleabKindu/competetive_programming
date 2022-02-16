# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        strt=fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            previous=slow
            slow=slow.next
        previous.next=None
        prev=None  
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        res=pv=ListNode(0)
        while strt and prev:
            temp=strt.next
            temp1=prev.next
            
            pv.next=strt
            strt.next=prev
            pv=pv.next.next
            
            
            strt=temp
            prev=temp1
        if not strt and prev:
            pv.next=prev
        elif not prev and strt:
            pv.next=strt
        return res.next
            
        
        