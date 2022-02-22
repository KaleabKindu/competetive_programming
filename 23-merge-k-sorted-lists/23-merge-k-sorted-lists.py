# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for i  in lists:
            head=i
            while head:
                heappush(heap,head.val)
                head=head.next
        ans=previous=ListNode(0)
        while heap:
            newNode=ListNode(heappop(heap))
            previous.next=newNode
            previous=newNode
        return ans.next
            
        