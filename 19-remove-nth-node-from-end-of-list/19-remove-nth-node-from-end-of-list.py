# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.count = 1
        cur = ListNode()
        cur.next = head
        def remove(node = cur):
            if node.next == None:
                return None if self.count == n else node
            nxt = remove(node.next)
            node.next = nxt
            self.count += 1
            if self.count != n:
                return node
            else:
                temp = node.next
                node.next = None
                return temp
        remove()
        return cur.next
        
            
            
            