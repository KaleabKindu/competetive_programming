# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next
        n = len(nodes)
        l = 0
        r = n - 1
        while l < k - 1:
            l += 1
            r -= 1
        nodes[l].val, nodes[r].val = nodes[r].val, nodes[l].val
        return head
            
            