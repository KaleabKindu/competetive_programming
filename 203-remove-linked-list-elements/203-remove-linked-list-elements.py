# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        answer = ListNode(next = head)
        previous = answer
        while current:
            if current.val == val:
                previous.next = current.next
                current.next = None
                current = previous.next
            else:
                previous = current
                current = current.next
        
        return answer.next
    
    
    
# Time Complexity = O(n)
# Space Complexity = O(1)
            