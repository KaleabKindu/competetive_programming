class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        merged = []
        i, j = 0, 0
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
                
        while i < n or j < m:
            if i < n:
                merged.append(nums1[i])
                i += 1
            elif j < m:
                merged.append(nums2[j])
                j += 1
        median = 0
        if (n + m) % 2 == 1:
            median = merged[(n + m)//2]
        else:
            median = (merged[(n + m)//2] + merged[((n + m)//2) - 1]) / 2
            
        return median