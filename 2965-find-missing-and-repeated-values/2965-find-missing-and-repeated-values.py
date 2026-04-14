class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        optlist = []
        n = len(grid)**2
        seen = set()

        for i in grid:
            for j in i:
                optlist.append(j)
        setsum = sum(set(optlist))        

        total = (n*(n+1))//2
        actualsum = sum(optlist)
        twice = total - actualsum
        missing = total - setsum

        if twice > 0:
            twice = missing - twice        
        if twice < 0:
            twice = (twice*(-1))+ missing
            
        return [twice, missing]