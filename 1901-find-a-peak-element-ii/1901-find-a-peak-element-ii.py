class Solution:

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
            start = 0
            end = len(mat) - 1
            while start < end:
                mid = (start + end)//2
                maxx = max(mat[mid])
                index = mat[mid].index(maxx)
                top_max = max(mat[mid - 1]) if mid - 1 >= 0 else -1
                bottom_max = max(mat[mid + 1]) if mid + 1 < len(mat) else -1
                if  top_max < mat[mid][index] > bottom_max:
                    return [mid, index]
                elif maxx < top_max:
                    end = mid
                else:
                    start = mid + 1
            return [start, mat[start].index(max(mat[start]))]
                    
        























    # def sermat(self,nums,column):
    #     start = 0
    #     end = len(nums) - 1
    #     while start <= end:
    #         mid = (start + end)//2
    #         if mid == 0 or nums[mid][column] > nums[mid - 1][column]:
    #             answer = mid
    #             start = mid + 1
    #         else:
    #             end = mid - 1
    #     return answer
    # def search(self, nums):
    #     start = 0
    #     end = len(nums) - 1
    #     while start <= end:
    #         mid = (start + end)//2
    #         if mid == 0 or nums[mid] > nums[mid - 1]:
    #             answer = mid
    #             start = mid + 1
    #         else:
    #             end = mid - 1
    #     return answer 
                
            
     # for i in range(len(mat)-1):
     #        row = self.search(mat[i])
     #        top = mat[i + 1][row] if i > 0 else -1
     #        bottom = mat[i - 1][row] if i > 0 else -1
     #        if top < mat[i][row] > bottom:
     #            return [i,row]

            # column = self.sermat(mat, row)
            # if mat[column][row] < bottom or mat[column][row] < top:
            #     continue
            
#             if mat[i][row] == mat[column][row]:
#                 return [column, row]
        