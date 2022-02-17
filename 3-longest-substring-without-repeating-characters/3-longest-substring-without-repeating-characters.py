class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=end=0
        dic={x: 0 for x in s}
        maxx=0
        while end<len(s):
            dic[s[end]]+=1
            while end < len(s) and dic[s[end]]<1:
                end+=1
                dic[s[end]]+=1
            while dic[s[end]]!=1:
                dic[s[start]]-=1
                start+=1
            end+=1   
            maxx=max(end-start,maxx)
        return maxx
            
            
            
            
            
        