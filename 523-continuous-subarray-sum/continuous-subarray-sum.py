class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
       pre=0
       maps={0:-1}
       for i,num in enumerate(nums):
          pre+=num
          h=pre%k
          if h in maps:
             if i-maps[h]>=2:
                 return True
          else:
             maps[h]=i       
       return False
                 

