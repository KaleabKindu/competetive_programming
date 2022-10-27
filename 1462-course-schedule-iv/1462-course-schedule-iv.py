class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        degree = [0]*numCourses
        for course_1, course_2 in prerequisites:
            graph[course_1].add(course_2)
            degree[course_2] += 1
        queue = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
                
        parents = defaultdict(set)
        while queue:
            course = queue.popleft()
            for neighbor in graph[course]:
                degree[neighbor] -= 1
                parents[neighbor].add(course)
                parents[neighbor].update(parents[course])
                if degree[neighbor] == 0:
                    queue.append(neighbor)

        answer = []
        for course_1,course_2  in queries:
            answer.append(course_1 in parents[course_2])

        return answer
            
                    