class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        n = len(instructions)
        
        r, c = 0, 0
        directions = {1: [0, 1], -1:[0, -1], 2:[1, 0], -2:[-1, 0]}
        left = {1:-2, -2:-1, -1:2, 2:1}
        right = {1:2, 2:-1, -1:-2, -2:1}
        direction = 1
        for i in range(n):
            char = instructions[i]
            if char == 'G':
                DIR = directions[direction]
                r, c = r + DIR[0], c + DIR[1]
            elif char == 'L':
                direction = left[direction]
            elif char == 'R':
                direction = right[direction]
        if direction == 1 and (r or c):
            return False
        return True