class Solution:
    def smallnum(self, n: int, t: int) -> int:
        i = n
        
        while True:
            p = 1
            temp = i
            
            if temp == 0:
                p = 0
            
            while temp > 0:
                dig = temp % 10
                p *= dig
                temp //= 10
            
            if p % t == 0:
                return i
            
            i += 1
