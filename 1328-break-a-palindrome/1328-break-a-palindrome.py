class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        size = len(palindrome)
        if size == 1:
            return ""
        for i in range(size):
            if size %  2 != 0 and i == size//2:
                continue
            if palindrome[i] != "a":
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        
        return palindrome[:-1] + "b"
                
        