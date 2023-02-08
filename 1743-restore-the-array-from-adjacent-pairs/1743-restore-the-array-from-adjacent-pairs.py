class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs)
        graph = defaultdict(list)
        for num1, num2 in adjacentPairs:
            graph[num1].append(num2)
            graph[num2].append(num1)
        initial = sorted(graph, key=lambda x: len(graph[x]))[0]
        seen = set([initial])
        answer = [initial]
        while len(answer) < n + 1:
            for node in graph[answer[-1]]:
                if node not in seen:
                    answer.append(node)
                    seen.add(node)
        return answer
                    