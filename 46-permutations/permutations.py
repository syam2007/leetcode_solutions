class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations as p
        r=list(p(nums))
        return r