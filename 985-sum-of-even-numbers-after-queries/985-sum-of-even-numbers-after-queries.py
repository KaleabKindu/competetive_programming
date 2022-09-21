class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = sum(num for num in nums if num % 2 == 0)
        n = len(queries)
        answer = []
        for i in range(n):
            val, index = queries[i]
            if nums[index] % 2 == 0:
                even -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                even += nums[index]
            answer.append(even)
        return answer
                
            