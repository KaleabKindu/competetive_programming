class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        n = len(blocks)
        operations = 0
        
        answer = float('inf')
        l, r = 0, 0
        while r < n:
            if r - l + 1 <= k:
                if blocks[r] == 'W':
                    operations += 1
                r += 1
                if r - l == k:
                    answer = min(answer, operations)
            else:
                if blocks[l] == 'W':
                    operations -= 1
                l += 1
        return answer
            