class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        answer = True
        for char in ransomNote:
            if char in count and count[char] > 0:
                count[char] -= 1
            else: answer = False
        return answer

    
# Time Complexity = O(n)  n = max(len(ransomeNote), len(magazine))
# Space Complexity = O(m) m = len(magazine)