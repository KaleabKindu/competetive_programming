"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        start = 1
        end = 1000 
        answer = []
        while start <= 1000 and end >= 1:
            temp = customfunction.f(start, end)
            if temp > z:
                end = end - 1
            elif temp < z:
                start = start + 1
            else:
                answer.append([start, end])
                end = end - 1
        return answer
                
                    
    