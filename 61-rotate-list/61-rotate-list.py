# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return None 
        
        end = head
        n = 1
        while end.next:
            end = end.next
            n += 1
        k = k % n
        if k == 0:
            return head
        
        cur = head
        temp = None
        for i in range(n - k - 1):
            cur = cur.next
        start = cur.next
        cur.next = None
        end.next = head
        
        return start
        
            
        
