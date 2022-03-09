class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @lru_cache()
        def mincost(index):
            if index >= len(cost) - 1:
                return cost[index] if index < len(cost) else 0
            oneStep = mincost(index + 1)
            twoStep = mincost(index + 2)
            
            return cost[index] + min(oneStep, twoStep)
        
        one = mincost(0)
        two = mincost(1)
        return min(one, two)
                
        