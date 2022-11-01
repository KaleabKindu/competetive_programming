class Solution:
    def allPathsSourceTarget(self, _graph: List[List[int]]) -> List[List[int]]:
        n = len(_graph)
        graph = defaultdict(list)
        for index in range(n):
            for node in _graph[index]:
                graph[index].append(node)
            
        answer = []
        path = [0]
        def dfs(node = 0):
            if node == n - 1:
                answer.append(path[:])
                return 
            for child in graph[node]:
                path.append(child)
                dfs(child)
                path.pop()
                
        dfs()
        
        return answer
        
        
            