# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=slow=head
        while fast:
            fast=fast.next.next
            slow=slow.next
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        maxx=-1
        while prev:
            if (prev.val + head.val) > maxx:
                maxx=prev.val + head.val
            prev=prev.next
            head=head.next
        return maxx
            
        
        
        
        # arr=[]
        # while head:
        #     arr.append(head.val)
        #     head=head.next
        # maxx=-1
        # for i in range(len(arr)//2):
        #     num=arr[i] + arr[len(arr)-1-i] 
        #     if num > maxx :
        #         maxx=num
        
        