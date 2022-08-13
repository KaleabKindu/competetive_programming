class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        answer = []
        
        while j < n and i < m:
            if nums1[i] <= nums2[j]:
                answer.append(nums1[i])
                i += 1
            else:
                answer.append(nums2[j])
                j += 1
        if i >= m:
            for k in range(j,len(nums2)):
                answer.append(nums2[k])
        elif j >= n:
            for k in range(i, len(nums1)):
                answer.append(nums1[k])
        
        for i in range(len(nums1)):
            nums1[i], answer[i] = answer[i], nums1[i]