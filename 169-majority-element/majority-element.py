class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k=len(nums)//2
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
            if f[i]>k:    
                return i
             