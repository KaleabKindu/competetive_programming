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
            visited.add(crse)
            path.add(crse)
            for neighbor in graph[crse]:
                if neighbor in path:
                    self.cycle = True
                if neighbor not in visited:
                    dfs(neighbor)
            stak.append(crse)
            path.remove(crse)
        for i in range(numCourses):
            if i not in visited:
                dfs(i)
        return stak if not self.cycle else []