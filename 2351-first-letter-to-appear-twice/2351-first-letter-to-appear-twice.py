class Solution:
    def repeatedCharacter(self, s: str) -> str:
        characters = set()
        for char in s:
            if char in characters:
                return char
            characters.add(char)