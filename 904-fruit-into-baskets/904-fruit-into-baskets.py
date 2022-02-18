class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start=maxx=end=0
        charset=set()
        while end<len(fruits):
            if len(charset)<2 or fruits[end] in charset:
                    charset.add(fruits[end])
                    maxx=max(end-start+1,maxx)
            else:
                lastone=fruits[end-1]
                for i in range(end-2,-1,-1):
                    if fruits[i]!=lastone:
                        start=i+1
                        if fruits[i] in charset:
                            charset.remove(fruits[i])
                        break
                charset.add(fruits[end])
                maxx=max(end-start+1,maxx)
            end+=1
        
        
        return maxx

        