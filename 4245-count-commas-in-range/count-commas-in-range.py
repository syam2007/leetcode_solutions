class Solution:
    def countCommas(self, n: int) -> int:
      c=0  
      for i in range(1,n+1):
         if i>999:
             c+=1
      return c