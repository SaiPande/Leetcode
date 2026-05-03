class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxcapacity, l, r = 0, 0, n-1

        while (l < r):
            maxcapacity = max(maxcapacity, min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1   
        
        return maxcapacity            