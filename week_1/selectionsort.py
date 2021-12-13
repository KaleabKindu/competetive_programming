class Solution: 
    def selectionSort(self, arr,n):
        for i in range(n-1):
            min=i+1
            for j in range(i+1,n):
                if arr[j] < arr[min]:
                    min=j
            if arr[min] < arr[i]:
                arr[i], arr[min]= arr[min],arr[i]
        return arr
          
