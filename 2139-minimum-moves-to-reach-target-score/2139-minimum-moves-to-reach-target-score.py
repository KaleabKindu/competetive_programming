class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        number = 1
        moves = 0
        while target != 1:
            if maxDoubles <= 0:
                moves += target - 1
                break
            elif target % 2 == 0:
                moves += 1
                maxDoubles -= 1
                target //= 2
            elif maxDoubles > 0:
                moves += 2
                target //= 2
                maxDoubles -= 1
        return moves
        
# Time Complexity = O(n)
# Space Complexity = O(1)
            