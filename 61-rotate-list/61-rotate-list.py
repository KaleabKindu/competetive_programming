# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        nodes = deque()
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        n = len(nodes)
        for i in range(k % n):
            temp = nodes.pop()
            nodes[-1].next = None
            temp.next = nodes[0]
            nodes.appendleft(temp)
        
        return nodes[0]
            
            