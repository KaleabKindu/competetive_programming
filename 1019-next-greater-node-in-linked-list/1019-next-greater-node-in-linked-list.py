# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        array=[]
        while head:
            array.append(head.val)
            head=head.next
        stak=[]
        output=[0 for i in array]
        for i in range(len(array)):
            while stak != [] and array[stak[-1]]<array[i]:
                output[stak.pop()]=array[i]
            stak.append(i)
        return output
        