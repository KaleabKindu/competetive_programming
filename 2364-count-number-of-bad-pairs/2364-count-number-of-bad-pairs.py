class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        unique = defaultdict(int)
        for i in range(n):
            unique[i - nums[i]] += 1
        
        if len(unique) < 2:
            return 0
        
        total = sum(unique.values())
        pairs = factorial(total) // (2 * factorial(total - 2))
        for value in unique.values():
            if value >= 2:
                invalid_pairs = factorial(value) // (2 * factorial(value - 2))
                pairs -= invalid_pairs
            
        return pairs
            
            