class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=maxx=end=0
        charset=set()
        while end<len(s):
            if s[end] not in charset:
                charset.add(s[end])
                end+=1
            else:
                charset.remove(s[start])
                start+=1
            maxx=max(end-start,maxx)
            
        return maxx       
            
            
            
            
            
        