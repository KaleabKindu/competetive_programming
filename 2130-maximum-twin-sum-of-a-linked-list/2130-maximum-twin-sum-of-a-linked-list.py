# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        maxx=-1
        for i in range(len(arr)//2):
            num=arr[i] + arr[len(arr)-1-i] 
            if num > maxx :
                maxx=num
        return maxx
        