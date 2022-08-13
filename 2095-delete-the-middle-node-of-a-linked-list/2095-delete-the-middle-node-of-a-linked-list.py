# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None
        
        fast = head
        slow = head
        previous = None
        while fast and fast.next:
            fast = fast.next.next
            previous = slow
            slow = slow.next
        previous.next = slow.next
        slow.next = None
        
        return head
    
    
# Time Complexity = O(log(n))
# Space Complexity = O(n)