# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        current = head
        while current:
            current = current.next
            n += 1
        
        part_size = n // k if k <= n else 1
        extra = n % k if n >= k else 0
        parts = []
        current = head
        while len(parts) < k:
            part = previous = current_part = ListNode()
            length = 0
            while current and length < part_size + min(extra, 1):
                current_part.next = current
                current_part = current_part.next
                previous = current
                current = current.next
                length += 1
            if extra > 0: extra -= 1
            parts.append(part.next)
            previous.next = None
                
        return parts
            
            