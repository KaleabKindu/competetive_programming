class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        maxScore = 0
        l = 0
        r = len(tokens) - 1
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
            elif score >= 1:
                power += tokens[r]
                score -= 1
                r -= 1
            else: break

            maxScore = max(maxScore, score)
            
        return maxScore if tokens else 0