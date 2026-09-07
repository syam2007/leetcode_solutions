class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        h=[]
        for i in nums:
           h.append(i*i)
        h.sort()  
        return h 