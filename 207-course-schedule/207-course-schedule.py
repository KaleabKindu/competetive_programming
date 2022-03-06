class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course_1, course_2 in prerequisites:
            graph[course_1].append(course_2)
        visited = set()
        def dfs(crse):
            if not graph[crse]:
                return True
            if crse in visited:
                return False
            visited.add(crse)
            for course in graph[crse]:
                if not dfs(course): return False
            graph[crse] = []
            return True
                
        for i in range(numCourses):
               if not dfs(i): return False
        return True