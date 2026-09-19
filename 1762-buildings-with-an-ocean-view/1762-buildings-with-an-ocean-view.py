class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        
        output = []
        maxbuld = 0

        for i in range(len(heights)-1, -1,-1):
            if heights[i]>maxbuld:
                output.append(i)
            # else:
            #     output.append(heights[i]-maxbuld)    
            maxbuld = max(maxbuld, heights[i])

        output.reverse()

        return output  