# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        less = []
        greater = []
        cur = head
        while cur:
            if cur.val >= x:
                greater.append(cur)
            else:
                less.append(cur)
            cur = cur.next
        if len(less) >= 2:
            l, r = 0, 1
            while r < len(less):
                less[l].next = less[r]
                l += 1
                r += 1
        if len(greater) >= 2:
            l, r = 0, 1
            while r < len(greater):
                greater[l].next = greater[r]
                l += 1
                r += 1
        answer = None
        if less and greater:
            less[-1].next = greater[0]
            greater[-1].next = None
            answer = less[0]
        elif not less:
            greater[-1].next = None
            answer = greater[0]
        elif not greater:
            less[-1].next = None
            answer = less[0]
        return answer
                
                
                