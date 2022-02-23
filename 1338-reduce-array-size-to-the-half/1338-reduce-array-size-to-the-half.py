class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total=len(arr)
        frequency=collections.Counter(arr)
        sorted_counts = sorted([v for v in frequency.values()], reverse = True)
        count=0
        for i in sorted_counts:
            total-=i
            count+=1
            if total<=len(arr)/2:
                return count
                    
  
        