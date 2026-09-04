class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
       n=len(nums)
       k=sum(nums)
       prefix = [0] * len(nums)

       prefix[0] = nums[0]

       for i in range(1, n):
         prefix[i] = prefix[i - 1] + nums[i]
       for i in range(n):
         if prefix[i]-nums[i]==k-prefix[i]:
             return i
       return -1     
           
 