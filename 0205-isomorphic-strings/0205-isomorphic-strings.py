class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        
        mapping = {}
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]: return False
            else: mapping[s[i]] = t[i]
        return True