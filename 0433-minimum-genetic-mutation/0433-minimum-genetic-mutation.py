
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        genes = set(['A','T','G','C'])
        queue = deque([(list(start), 0)])
        visited = set([tuple(start)])
        while queue:
            current_sequence, mutations = queue.popleft()
            if "".join(current_sequence) == end:
                return mutations
            for i in range(len(current_sequence)):
                original_gene = current_sequence[i]
                for new_gene in genes:
                    if new_gene != original_gene:
                        current_sequence[i] = new_gene
                        if tuple(current_sequence) not in visited and "".join(current_sequence) in bank:
                            queue.append((current_sequence[:], mutations + 1))
                            visited.add(tuple(current_sequence))
                        current_sequence[i] = original_gene
        return -1
                
                
        
                

        
        