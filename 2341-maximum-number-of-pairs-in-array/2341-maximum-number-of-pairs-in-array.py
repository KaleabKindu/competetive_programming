class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = 0
        leftovers = 0
        count = Counter(nums)
        for i in count:
            if count[i] % 2 == 0:
                pairs += count[i]// 2
            else: 
                pairs += count[i] // 2
                leftovers += count[i] % 2
        return [pairs, leftovers]
        