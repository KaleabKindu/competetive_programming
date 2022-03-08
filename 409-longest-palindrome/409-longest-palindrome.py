class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        length = 0
        seenOdd = False
        for characters in count.values():
            if characters % 2 == 0:
                length += characters
            else:
                length += characters - 1 
                seenOdd = True
                
        return length + 1 if seenOdd else length