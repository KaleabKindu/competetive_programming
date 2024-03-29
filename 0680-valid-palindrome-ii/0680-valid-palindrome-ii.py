class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        start = 0
        end = len(s) - 1
        while start <= end:
            if s[start] != s[end]:
                return check(start + 1, end) or check(start, end - 1)
            
            start += 1
            end -= 1
            
        return True
        