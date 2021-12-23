class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
            stack=[]
            dct={}
            ans=[]
            for i in range(len(nums2)):
                if (len(stack)==0 or stack[-1]>nums2[i]):
                    stack.append(nums2[i])
                    continue
                while len(stack)>0 and stack[-1]<nums2[i]:
                    dct[stack.pop()]=nums2[i]  
                stack.append(nums2[i])
            for i in nums1:
                if i not in dct:
                    ans.append(-1)
                else:
                    ans.append(dct[i])
            return(ans)
