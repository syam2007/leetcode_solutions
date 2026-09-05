class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k=0
        h=0
        for i in nums:
            if i==1:
                k=k+1
                h=max(h,k)
            else:
                k=0               
        return h        