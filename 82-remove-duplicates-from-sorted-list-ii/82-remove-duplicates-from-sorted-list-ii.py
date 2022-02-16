# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=prev=ListNode(0)
        cur=head
        while cur:
            temp=cur.next
            if temp and cur.val == temp.val:
                while temp and cur.val == temp.val:
                    temp=temp.next
                prev.next=temp
            else:
                prev.next=cur
                prev=prev.next
            cur=temp
        return node.next
            
            
        
        
        
        
        
        
        
#         while cur:
#             temp=cur.next
#             # print(temp)
#             if temp and cur.val!=temp.val:
#                 prev.next=cur
#                 prev=prev.next
#                 cur=cur.next
#                 # print(cur)
#                 continue
                
#             while temp and cur.val == temp.val:
#                 temp=temp.next
#             if not temp:
#                 prev.next=None
#                 cur=None
#                 continue
#             # prev.next=temp
#             # prev=prev.next
#             if not temp.next:
#                 prev.next=temp
#             cur=temp
#             # print(node)   
#         return node.next    
                
        
        
        
        
        
        
        
        
        
        # cur=res=head
        # while cur:
        #     nex=cur.next
        #     if  cur.val != nex.val:
        #         prev=cur
        #         cur=cur.next
        #         continue
        #     while cur.val==nex.val:
        #         nex=nex.next
        #     cur.next=nex.next
        #     prev=cur
        #     cur=cur.next
        # return res
        