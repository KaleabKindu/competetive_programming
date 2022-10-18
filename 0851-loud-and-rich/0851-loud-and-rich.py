class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        in_degree = [0 for i in range(n)]
        answer = [i for i in range(n)]
        
        for person_1, person_2 in richer:
            graph[person_1].append(person_2)
            in_degree[person_2] += 1
            
        
        queue = deque()
        for index, person in enumerate(in_degree):
            if in_degree[index] == 0:
                queue.append(index)
                
        while queue:
            current_person = queue.popleft()
            
            for neighbor in graph[current_person]:  
                if quiet[answer[current_person]] < quiet[answer[neighbor]]:
                    answer[neighbor] = answer[current_person]
                    
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return answer