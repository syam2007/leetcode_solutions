class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k=set()
        for i in nums1:
            if i in nums2:
                k.add(i)
        return list(k)        
