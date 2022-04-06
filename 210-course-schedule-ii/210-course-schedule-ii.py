class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        degree = {x: 0 for x in range(numCourses)}
        for course_1, course_2 in prerequisites:
            graph[course_1].add(course_2)
            degree[course_2] += 1
        queue = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        top_sort = []
        while queue:
            cur = queue.popleft()
            top_sort.append(cur)
            for neighbor in graph[cur]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return top_sort[::-1] if len(top_sort) == numCourses else []
            
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        