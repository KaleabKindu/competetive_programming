
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        seen = set()
        def dfs(src, trg):
            seen.add(src)
            if src == trg:
                return True
            for n in graph[src]:
                if n not in seen:
                    if dfs(n, trg):
                        return True
            return False
        
        for head, tail in edges:
            seen.clear()
            if head in graph and tail in graph and dfs(head, tail):
                return [head, tail]
            
            graph[head].add(tail)
            graph[tail].add(head)
        