class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(set)
        n = len(equations)
        for i in range(n):
            equation = equations[i]
            graph[equation[0]].add((equation[1], values[i]))
            graph[equation[1]].add((equation[0], 1/values[i]))
        visited = set()
        def dfs(variable, destination, value = 1.0):
            visited.add(variable)
            if variable in graph and variable == destination:
                return value
            val = -1
            for neighbor, weight in graph[variable]:
                if neighbor not in visited:
                    val = max(val, dfs(neighbor, destination, value * weight))
            return val
        answer = []
        for query in queries:
            answer.append(dfs(query[0], query[1]))
            visited.clear()
        return answer