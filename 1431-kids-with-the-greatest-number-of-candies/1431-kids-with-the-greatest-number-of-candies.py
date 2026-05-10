class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        extracandy = [extraCandies + i for i in candies]

        maxnum = max(candies)
        optarr = []
        for i in extracandy:
            if i < maxnum:
                optarr.append(False)
            else:
                optarr.append(True)
        return optarr            