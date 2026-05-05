class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        totalcandies = len(candyType)//2
        candytypes = len(set(candyType))

        if totalcandies >= candytypes:
            return candytypes
        else:
            return totalcandies    
        