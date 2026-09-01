class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        area=0
        while l<r:
            h=min(height[l],height[r])
            width=r-l
            area=max(area,h*width)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area           
