class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(i = 0, char = '', count = 0, remains = k):
            
            if i == len(s):
                return 0
            
            
            cost = inf
            if remains > 0:
                cost = dp(i+1, char, count, remains - 1)
            
            letter = s[i]
            
            kcost = inf
            if letter == char:
                add = 0
                
                if count == 1 or len(str(count + 1)) > len(str(count)):
                    add = 1
                
                kcost = add + dp(i+1, letter, count + 1, remains)
            else:
                kcost = 1 + dp(i+1, letter, 1, remains)
            
            return min(kcost, cost)
                
            
        return dp()
        
#         n = len(s)
        
#         characters = []
#         length = 0

#         i = 0
#         while i < n:
#             j = i
#             while j < n and s[i] == s[j]:
#                 j += 1
#             characters.append(j - i)
#             char = len(str(characters[-1]))
#             if j - i > 1:
#                 length += char + 1
#             else:
#                 length += 1
#             i = j
        
#         cost = []
#         for i in range(len(characters)):
#             if characters[i] > 10:
#                 if characters[i] - 10 <= k:
#                     cost.append(characters[i] - 10)
#             else:
#                 if characters[i] - 1 <= k + 1:
#                     cost.append(characters[i] - 1)
                    
#         cost.sort()         
#         for i in range(len(cost)):
#             k -= cost[i]
#             if k > 0:
#                 length -= 1
#         return length