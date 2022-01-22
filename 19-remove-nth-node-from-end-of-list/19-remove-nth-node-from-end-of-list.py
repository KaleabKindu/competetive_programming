# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        count=0
        while cur:
            cur = cur.next
            count+=1
        if count==1:
            return None
        elif count==n:
            return head.next
        curr = head.next
        prev = head        
        i = 2
        while count - i != n-1 :
            prev = curr
            curr  = curr.next
            i += 1 
        prev.next = curr.next
        curr.next = None
            
        return head 
        
      
            
            
            
            
        
        
        
        
        
            