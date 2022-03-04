import re
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        graph = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                graph[pattern].append(word)
        
        visited = set([beginWord])
        queue = deque([(beginWord, 0)])
        move = 1
        
        while queue:
            word, move = queue.popleft()
            if word == endWord:
                return move + 1
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for neighbor in graph[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, move + 1))
        return 0
        
        
        



            
                