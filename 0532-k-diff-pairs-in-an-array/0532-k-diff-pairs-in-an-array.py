class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        frequency = Counter(nums)
        n = len(nums)
        pairs = 0
        for i in range(n):
            if nums[i] - k in frequency:
                if not k:
                    if frequency[nums[i]] > 1:
                        pairs += 1
                else:
                    pairs += 1
                frequency.pop(nums[i] - k)
        
        return pairs
            
            