class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        size = n = len(senate)
        rights = defaultdict()
        for i in senate:
            rights[i] = rights.get(i, 0) + 1
        
        jump = set()
        index = rjump = djump = 0 
        while n > 1:
            i = index % size
            if senate[i] == "R" and i not in jump:
                if rjump == 0:
                    rights["D"] = rights.get("D", 0)- 1
                    djump += 1
                    n -= 1
                else:
                    jump.add(i)
                    rjump -= 1
            elif senate[i] == "D" and i not in jump:
                if djump == 0:
                    rights["R"] = rights.get("R", 0)- 1
                    rjump += 1
                    n -= 1
                else:
                    jump.add(i)
                    djump -= 1
            index += 1
            
        return "Radiant" if rights.get("R", 0) > rights.get("D", 0) else "Dire"
        
                
        
        

            
        
  
     