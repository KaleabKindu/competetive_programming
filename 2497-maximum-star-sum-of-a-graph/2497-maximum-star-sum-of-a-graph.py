class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        graph = defaultdict(list)
        values = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            values[a].append(vals[b])
            graph[b].append(a)
            values[b].append(vals[a])
            
        star_sum = float('-inf')
        for node in range(n):
            temp = sorted(values[node], reverse=True)
            ssum = 0
            prefix = 0
            for i in range(min(k, len(temp))):
                prefix += temp[i]
                ssum = max(ssum, prefix)

            star_sum = max(star_sum, ssum + vals[node])

        return star_sum 
                
                
        
        