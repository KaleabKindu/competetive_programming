# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.begin = None
        self.end = None
        self.j = 1
        def getElements(node = head, i = 1):
            if i == k:
                self.begin = node
            if node.next == None:
                if self.j == k:
                    self.end = node
                return
            getElements(node.next, i + 1)
            self.j += 1
            if self.j == k:
                self.end = node
        getElements()
        self.begin.val, self.end.val = self.end.val, self.begin.val
        return head
            