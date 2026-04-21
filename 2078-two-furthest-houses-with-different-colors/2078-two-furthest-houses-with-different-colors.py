class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        maxt = 0
        i = 0
        j = len(colors)-1
        while i<j and j<len(colors):
            if colors[i] != colors[j]:
                maxt=max(j-i,maxt)
            if j == i + 1:
                i += 1
                j = len(colors) - 1
            else:
                j -= 1
        return maxt                