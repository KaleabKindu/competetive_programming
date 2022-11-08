class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        properties.sort(key=lambda x: (x[0], -x[1]))
        weak_characters = 0
        stack = []
        for start, end in properties:
            while stack and start > stack[-1][0] and end > stack[-1][1]:
                stack.pop()
                weak_characters += 1
            stack.append([start, end])
        return weak_characters
        