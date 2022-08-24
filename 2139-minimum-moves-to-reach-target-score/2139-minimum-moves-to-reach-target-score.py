class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        moves = 0
        while target != 1:
            if target % 2 != 0:
                target -= 1
                moves += 1
            else:
                if maxDoubles > 0:
                    target /= 2
                    moves += 1
                    maxDoubles -= 1
                else:
                    moves += target - 1
                    break
        return int(moves)
        