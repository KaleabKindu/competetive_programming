# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        link=val=ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                link.next=list1
                list1=list1.next
                
            else:
                link.next=list2
                list2=list2.next
            link=link.next
        link.next = list1 or list2

        return val.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if not head.next.next:
            if head.val > head.next.val:
                head.val,head.next.val=head.next.val,head.val
            return head
        st=fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=None
        # print(st)
        # print(slow)
        right=self.sortList(st)
        left=self.sortList(slow)
        # print(right)
        # print(left)
        res=self.mergeTwoLists(right,left)
        return res
        
                
            
                
            
            
            
            
                
            