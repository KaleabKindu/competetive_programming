class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        stak = []
        self.cycle = False
        visited = set()
        path = set()
        def dfs(crse):
            if crse in path:
                return True
            path.add(crse)
            for neighbor in graph[crse]:
                if neighbor not in visited:
                    if dfs(neighbor): return True
            stak.append(crse)
            path.remove(crse)
            visited.add(crse)
            return False
        for i in range(numCourses):
            if i not in visited:
                if dfs(i): return []
        return stak 