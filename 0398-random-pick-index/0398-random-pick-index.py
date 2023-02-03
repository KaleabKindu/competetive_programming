class Solution:
    from random import randint
    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for i in range(len(nums)):
            self.indices[nums[i]].append(i)
    def pick(self, target: int) -> int:
        temp = self.indices[target]
        n = len(temp)
        return temp[randint(0, n - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)