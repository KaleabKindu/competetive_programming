class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stak=set()
        nums2 = set(nums2)
        for i in nums1:
            if i in nums2:
                stak.add(i)
        return list(stak)