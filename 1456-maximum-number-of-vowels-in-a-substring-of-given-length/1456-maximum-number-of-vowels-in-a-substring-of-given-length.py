class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        answer = 0
        vowels = set(['a','e','i','o','u'])
        window_vowels = 0
        l, r = 0, 0
        while r < n:
            if r - l + 1 <= k:
                if s[r] in vowels:
                    window_vowels += 1
                r += 1
                if r - l == k:
                    answer = max(answer, window_vowels)
            else:
                if s[l] in vowels:
                    window_vowels -= 1
                l += 1
        
        return answer