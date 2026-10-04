class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        count = 0
        for i in range(len(s)):
            if j<len(g) and g[j]<=s[i]:
                count += 1 
                j+=1    
        return count          