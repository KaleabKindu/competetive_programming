class Solution:
    def minimumBuckets(self, street: str) -> int:
        valid = lambda index: index - 1 >= 0 and index + 1 < len(street)
        house = buckets = 0
        collected = set()
        for i in range(len(street)):
            if street[i] == '.' and valid(i):
                if street[i - 1] == 'H' and street[i + 1] == 'H':
                    if i - 1 not in collected and i + 1 not in collected:
                        collected.add(i + 1)
                        collected.add(i - 1)
                        buckets += 1
            elif street[i] == 'H':
                house += 1
        for i in range(len(street)):
            if street[i] == 'H' and i not in collected:
                if i - 1 >= 0 and street[i - 1] == '.' :
                    collected.add(i)
                    buckets += 1
                elif i + 1 < len(street) and street[i + 1] == '.':
                    collected.add(i)
                    buckets += 1
                
        return -1 if len(collected) != house else buckets
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
#         Espace = defaultdict()
#         House = 0
#         for i in range(len(street)):
#             count = 0
#             if street[i] == '.':
#                 if i - 1 >= 0 and street[i - 1] == 'H':
#                     count += 1
#                 if i + 1 < len(street) and street[i + 1] == 'H':
#                     count+= 1
#                 Espace[i] = count
#             elif street[i] == 'H':
#                 House += 1
#         print(House, Espace)    
#         buckets = 0     
#         collected = set()
#         for i in range(len(street)):
#             if street[i] == '.' and Espace[i] == 2:
#                 collected.add(i - 1)
#                 collected.add(i + 1)
#                 buckets += 1
#         print(buckets, collected)
#         for i in range(len(street)):
#             if street[i] == 'H' and i not in collected:
#                 if i - 1 >= 0 and street[i - 1] == '.' and Espace[i - 1] == 1:
#                     collected.add(i)
#                     buckets += 1
#                 elif i + 1 < len(street) and street[i + 1] == '.' and Espace[i + 1] == 1:
#                     collected.add(i)
#                     buckets += 1
#         print(collected, buckets)
#         return -1 if len(collected) != House else buckets
                    
                
                
                
                
                
                
                
                
                
                
                
