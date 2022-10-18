# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:        
        answer = [[-1] * n for i in range(m)]
        
        # starting row or col for each move
        moves = [0, n - 1, m - 1, 0] # [right, down, left, up]

        current_num = head
        
        while current_num:
            right, down, left, up = moves
            # move to the right
            i = right
            while current_num and i < down + 1:
                answer[right][i] = current_num.val
                current_num = current_num.next
                i += 1
            right += 1
            
            # move down
            i = right
            while current_num and i < left + 1:
                answer[i][down] = current_num.val
                current_num = current_num.next
                i += 1
            down -= 1
            
            # move left
            i = down
            while current_num and i > up - 1:
                answer[left][i] = current_num.val
                current_num = current_num.next
                i -= 1
            left -= 1
            
            # move up
            i = left
            while current_num and i > right - 1:
                answer[i][up] = current_num.val
                current_num = current_num.next
                i -= 1

            up += 1
            moves = right, down, left, up 
            
        return answer
            
            
            
           
            
            
            
        