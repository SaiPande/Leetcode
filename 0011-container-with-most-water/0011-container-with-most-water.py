class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) -1
        maxval = 0
           
        while left<right:
            width = right-left
            length = min( height[left], height[right])

            if width*length > maxval:
                maxval = width*length

            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                if left+1 < right-1 and height[left+1] > height[right-1]:
                    left+=1
                else:
                    right-=1    
        return maxval                    