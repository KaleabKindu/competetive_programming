class Solution:          
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count=start=0 
        end=len(people)-1
        while start<=end:
            if people[end]+people[start]<=limit:
                end-=1
                start+=1
            else:
                end-=1
            count+=1
                
        
        return count
        
        
        
        
        
        
                
        