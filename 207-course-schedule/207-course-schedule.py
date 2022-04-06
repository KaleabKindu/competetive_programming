class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        degree = {x: 0 for x in range(numCourses)}
        for course_1, course_2 in prerequisites:
            graph[course_1].add(course_2)
            degree[course_2] += 1
        queue = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        top_sort = 0
        while queue:
            cur = queue.popleft()
            top_sort += 1
            for neighbor in graph[cur]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return True if top_sort == numCourses else False
            
            
    
        
        
            
            
            
       
            
