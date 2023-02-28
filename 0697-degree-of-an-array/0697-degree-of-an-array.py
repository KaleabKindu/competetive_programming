class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        degree = max(count.values())
        
        left = defaultdict(int)
        right = defaultdict(int)
        
        for i in range(n):
            right[nums[i]] = i
            if nums[i] not in left:
                left[nums[i]] = i
                
        answer = float('inf')
        for num in count:
            if count[num] >= degree:
                answer = min(answer, right[num] - left[num] + 1)
        return answer