class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        for key,value in f.items():
            if value==1:
                return key
